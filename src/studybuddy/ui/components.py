"""UI components for StudyBuddy Streamlit interface."""

import streamlit as st
import time
from typing import List, Optional

from .templates import CSS_STYLES, BOT_MESSAGE_TEMPLATE, USER_MESSAGE_TEMPLATE
from ..config.settings import settings


class UIComponents:
    """Handles UI components and rendering for StudyBuddy."""

    @staticmethod
    def render_header():
        """Render the enhanced application header."""
        st.markdown(
            """
        <div class="main-header">
            <h1>🎓 StudyBuddy</h1>
            <p>Your intelligent document companion for smarter studying</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_project_selector(project_manager, on_change_callback=None):
        """Render enhanced project selector."""
        projects = project_manager.get_project_list_for_selectbox()
        current_project = project_manager.get_current_project()

        if not projects:
            return None

        current_display = None
        if current_project:
            current_display = f"{current_project['emoji']} {current_project['name']}"

        # Enhanced project selector with header
        st.markdown('<div class="project-selector">', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-header">📂 Current Project</div>',
            unsafe_allow_html=True,
        )

        selected = st.selectbox(
            "Select your project",
            options=projects,
            index=projects.index(current_display) if current_display in projects else 0,
            key=f"project_selector_{st.session_state.project_selector_key}",
            label_visibility="collapsed",
        )

        # Show project description if available
        if current_project and current_project.get("description"):
            st.markdown(
                f'<p class="text-sm" style="margin: 0.5rem 0 0 0; color: #6b7280;">{current_project["description"]}</p>',
                unsafe_allow_html=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

        if selected:
            project_id = project_manager.get_project_id_from_display_name(selected)
            if project_id != st.session_state.current_project_id:
                project_manager.set_current_project(project_id)
                if on_change_callback:
                    on_change_callback()
                st.rerun()

        return selected

    @staticmethod
    def render_project_creation_form(project_manager):
        """Render enhanced project creation form."""
        st.markdown(
            '<div class="section-header">✨ Create New Project</div>',
            unsafe_allow_html=True,
        )

        with st.form("create_project_form", clear_on_submit=True):
            project_name = st.text_input(
                "Project name",
                placeholder="e.g., Advanced Calculus, Organic Chemistry",
                label_visibility="collapsed",
            )

            project_description = st.text_input(
                "Description (optional)",
                placeholder="Brief description of your project",
                label_visibility="collapsed",
            )

            col1, col2 = st.columns([2, 1])
            with col1:
                project_emoji = st.selectbox(
                    "Choose an icon",
                    options=settings.PROJECT_EMOJIS,
                    index=0,
                    label_visibility="collapsed",
                )

            with col2:
                submitted = st.form_submit_button(
                    "Create", use_container_width=True, type="primary"
                )

            if submitted and project_name.strip():
                project_id = project_manager.create_project(
                    name=project_name.strip(),
                    emoji=project_emoji,
                    description=project_description.strip(),
                )
                project_manager.set_current_project(project_id)
                st.session_state.project_selector_key += 1
                st.success(f"Created project: {project_emoji} {project_name}")
                time.sleep(1)
                st.rerun()

    @staticmethod
    def render_project_stats(project_manager):
        """Render enhanced project statistics."""
        current_project = project_manager.get_current_project()

        if current_project:
            st.markdown(
                '<div class="section-header">📊 Project Stats</div>',
                unsafe_allow_html=True,
            )

            files_count = len(current_project.get("file_names", []))
            has_chat = bool(current_project.get("conversation"))

            # Enhanced metrics with cards
            col1, col2 = st.columns(2)

            with col1:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div style="font-size: 1.5rem; font-weight: 600; color: #667eea;">📄 {files_count}</div>
                        <div style="font-size: 0.875rem; color: #6b7280;">Documents</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with col2:
                status_color = "#22c55e" if has_chat else "#f59e0b"
                status_text = "Ready" if has_chat else "Empty"
                status_emoji = "✅" if has_chat else "⚠️"

                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div style="font-size: 1.5rem; font-weight: 600; color: {status_color};">{status_emoji}</div>
                        <div style="font-size: 0.875rem; color: #6b7280;">{status_text}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    @staticmethod
    def render_welcome_screen():
        """Render enhanced welcome message."""
        st.markdown(
            """
            <div class="info-card">
                <div style="font-size: 2rem; margin-bottom: 1rem;">📚</div>
                <h3 style="margin: 0 0 0.5rem 0; color: #374151;">Welcome to StudyBuddy!</h3>
                <p style="margin: 0; color: #6b7280;">
                    Upload your study materials and start asking questions.<br>
                    Your AI study companion is ready to help you learn.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_file_upload_section():
        """Render enhanced file upload section."""
        current_project_id = st.session_state.get("current_project_id")

        if current_project_id:
            from ..core.project_manager import ProjectManager

            project_manager = ProjectManager()
            existing_files, existing_names = project_manager.get_project_files(
                current_project_id
            )

            # Show existing files with better styling
            if existing_files:
                st.markdown(f"**📁 Current Files ({len(existing_files)})**")
                with st.expander("View uploaded files", expanded=False):
                    for i, name in enumerate(existing_names, 1):
                        st.markdown(f"`{i}.` **{name}**")
            else:
                st.markdown("**📁 No files uploaded yet**")

        st.markdown("**Upload Documents**")
        pdf_docs = st.file_uploader(
            "Choose PDF files for this project",
            accept_multiple_files=True,
            type=["pdf"],
            label_visibility="collapsed",
            key=f"file_uploader_{current_project_id}",
            help="Upload PDF documents to start chatting",
        )

        if pdf_docs:
            st.success(f"✅ {len(pdf_docs)} file(s) ready to process")

        return pdf_docs

    @staticmethod
    def render_project_actions(project_manager):
        """Render enhanced project management actions."""
        current_project = project_manager.get_current_project()

        if current_project:
            st.markdown(
                '<div class="section-header">🛠️ Project Actions</div>',
                unsafe_allow_html=True,
            )

            col1, col2 = st.columns(2)

            with col1:
                if st.button(
                    "🧹 Clear Data",
                    type="secondary",
                    help="Clear documents and chat history",
                    use_container_width=True,
                ):
                    project_manager.clear_project_data(current_project["id"])
                    st.success("Project data cleared!")
                    time.sleep(1)
                    st.rerun()

            with col2:
                if len(project_manager.get_all_projects()) > 1:
                    if st.button(
                        "🗑️ Delete",
                        type="secondary",
                        help="Delete this project completely",
                        use_container_width=True,
                    ):
                        project_name = current_project["name"]
                        project_manager.delete_project(current_project["id"])
                        st.success(f"Deleted '{project_name}'")
                        time.sleep(1)
                        st.rerun()

    @staticmethod
    def render_sidebar_content(project_manager):
        """Render complete sidebar content."""
        # Project creation
        UIComponents.render_project_creation_form(project_manager)

        st.divider()

        # File upload
        current_project = project_manager.get_current_project()
        if current_project:
            st.markdown("**Documents**")
            pdf_docs = UIComponents.render_file_upload_section()

            # Process button
            if st.button("Process Documents", type="primary", use_container_width=True):
                return pdf_docs

            st.divider()

            # Project actions
            UIComponents.render_project_actions(project_manager)

        return None

    @staticmethod
    def render_main_chat_area(project_manager):
        """Render the main chat interface."""
        current_project = project_manager.get_current_project()

        # Project selector
        UIComponents.render_project_selector(project_manager)

        # Status
        UIComponents.render_status_indicator(st.session_state.conversation is not None)

        # Chat input
        col1, col2 = st.columns([5, 1])

        with col1:
            user_question = st.text_input(
                "Ask a question",
                placeholder="What would you like to know about your documents?",
                key="user_input",
                disabled=not current_project,
                label_visibility="collapsed",
            )

        with col2:
            send_button = st.button(
                "Send",
                type="primary",
                disabled=not current_project,
                use_container_width=True,
            )

        # Handle input
        if (user_question or send_button) and st.session_state.user_input.strip():
            return st.session_state.user_input

        return None

    @staticmethod
    def render_document_stats(document_count: Optional[int]):
        """Render minimal document statistics."""
        if document_count:
            st.metric("📄 Documents", document_count)

    @staticmethod
    def render_status_indicator(has_conversation: bool):
        """Render enhanced status indicator."""
        if not has_conversation:
            st.markdown(
                """
            <div class="status-indicator status-error">
                ⚠️ Upload documents to start chatting
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
            <div class="status-indicator status-ready">
                ✅ Ready to chat with your documents
            </div>
            """,
                unsafe_allow_html=True,
            )

    @staticmethod
    def render_chat_history(chat_history):
        """Render clean chat history."""
        if chat_history:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            for i, message in enumerate(chat_history):
                if i % 2 == 0:
                    st.write(
                        USER_MESSAGE_TEMPLATE.replace("{{MSG}}", message.content),
                        unsafe_allow_html=True,
                    )
                else:
                    st.write(
                        BOT_MESSAGE_TEMPLATE.replace("{{MSG}}", message.content),
                        unsafe_allow_html=True,
                    )
            st.markdown("</div>", unsafe_allow_html=True)
