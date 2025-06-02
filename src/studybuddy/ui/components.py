"""UI components for StudyBuddy Streamlit interface - Simple, clean design."""

import streamlit as st
import time
from typing import Optional

from .templates import CSS_STYLES, BOT_MESSAGE_TEMPLATE, USER_MESSAGE_TEMPLATE
from ..config.settings import settings


class UIComponents:
    """Simplified UI components for StudyBuddy."""

    @staticmethod
    def render_header():
        """Render simple app header."""
        st.markdown(
            """
        <div class="app-header">
            <h1>Study Buddy</h1>
            <p>Your AI study assistant</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_project_selector(project_manager):
        """Render simple project selector."""
        projects = project_manager.get_project_list_for_selectbox()
        current_project = project_manager.get_current_project()

        if not projects:
            return None

        current_display = None
        if current_project:
            current_display = f"{current_project['emoji']} {current_project['name']}"

        selected = st.selectbox(
            "Select Project",
            options=projects,
            index=projects.index(current_display) if current_display in projects else 0,
            key=f"project_selector_{st.session_state.project_selector_key}",
        )

        if selected:
            project_id = project_manager.get_project_id_from_display_name(selected)
            if project_id != st.session_state.current_project_id:
                project_manager.set_current_project(project_id)
                st.rerun()

        return selected

    @staticmethod
    def render_new_project_form(project_manager):
        """Render simple project creation form."""
        st.subheader("New Project")

        with st.form("new_project", clear_on_submit=True):
            col1, col2 = st.columns([3, 1])

            with col1:
                name = st.text_input("Name", placeholder="Project name")

            with col2:
                emoji = st.selectbox("Icon", options=settings.PROJECT_EMOJIS)

            if st.form_submit_button("Create Project", use_container_width=True):
                if name.strip():
                    project_id = project_manager.create_project(name.strip(), emoji)
                    project_manager.set_current_project(project_id)
                    st.session_state.project_selector_key += 1

                    st.markdown(
                        f"""
                        <div class="status status-success">
                            ✓ Created: {emoji} {name}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                    time.sleep(1)
                    st.rerun()

    @staticmethod
    def render_file_upload():
        """Render simple file upload."""
        current_project_id = st.session_state.get("current_project_id")

        # Show current file status
        if current_project_id:
            from ..core.project_manager import ProjectManager

            project_manager = ProjectManager()
            existing_files, existing_names = project_manager.get_project_files(
                current_project_id
            )

            if existing_files:
                st.markdown(
                    f"""
                    <div class="status status-success">
                        {len(existing_files)} files ready
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        return st.file_uploader(
            "Upload PDF Documents",
            accept_multiple_files=True,
            type=["pdf"],
            key=f"files_{current_project_id}",
        )

    @staticmethod
    def render_chat_input():
        """Render simple chat input."""
        return st.text_input(
            "Ask a question",
            placeholder="What would you like to know?",
            key="user_input",
        )

    @staticmethod
    def render_chat_history(chat_history):
        """Render simple chat history."""
        if chat_history:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            for i, message in enumerate(chat_history):
                if i % 2 == 0:
                    st.markdown(
                        USER_MESSAGE_TEMPLATE.replace("{{MSG}}", message.content),
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        BOT_MESSAGE_TEMPLATE.replace("{{MSG}}", message.content),
                        unsafe_allow_html=True,
                    )
            st.markdown("</div>", unsafe_allow_html=True)

    @staticmethod
    def render_welcome():
        """Render simple welcome message."""
        st.info("Upload PDF documents and start asking questions.")

    @staticmethod
    def render_sidebar(project_manager, chat_service):
        """Render simplified sidebar."""
        # Project selector
        UIComponents.render_new_project_form(project_manager)
        st.divider()

        # File upload
        st.subheader("Documents")
        pdf_docs = UIComponents.render_file_upload()

        if pdf_docs:
            if st.button("Process Documents", type="primary", use_container_width=True):
                return {"action": "process", "files": pdf_docs}

        st.divider()

        # Simple chatbot toggle
        st.subheader("Settings")
        simple_mode = st.checkbox(
            "Simple Chatbot Mode",
            value=st.session_state.get("simple_chatbot_enabled", False),
        )

        if simple_mode != st.session_state.get("simple_chatbot_enabled", False):
            st.session_state.simple_chatbot_enabled = simple_mode
            chat_service.toggle_simple_chatbot(simple_mode)

            if simple_mode:
                st.markdown(
                    """
                    <div class="status status-info">
                        Simple chatbot mode enabled
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        return None
