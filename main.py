"""Main application file for Study Buddy - Simple, clean design."""

import streamlit as st

# Import our modules
from src.studybuddy.core.document_processor import DocumentProcessor
from src.studybuddy.core.chat_service import ChatService
from src.studybuddy.core.project_manager import ProjectManager
from src.studybuddy.ui.components import UIComponents
from src.studybuddy.ui.templates import CSS_STYLES
from src.studybuddy.utils.helpers import (
    validate_environment,
    initialize_streamlit_config,
)


class StudyBuddyApp:
    """Study Buddy application with clean UI."""

    def __init__(self):
        self.document_processor = DocumentProcessor()
        self.chat_service = ChatService()
        self.project_manager = ProjectManager()
        self.ui = UIComponents()

    def setup_app(self):
        """Setup the application."""
        initialize_streamlit_config()

        if not validate_environment():
            st.stop()

        st.write(CSS_STYLES, unsafe_allow_html=True)
        self.chat_service.initialize_session_state()

    def process_documents(self, pdf_docs):
        """Process uploaded documents."""
        if not pdf_docs:
            st.warning("Please upload PDF files.")
            return

        with st.spinner("Processing documents..."):
            # Process documents
            vector_store = self.document_processor.process_documents(pdf_docs)
            if not vector_store:
                return

            # Create conversation
            conversation = self.chat_service.create_conversation_chain(vector_store)
            if not conversation:
                return

            # Update session
            st.session_state.conversation = conversation
            st.session_state.documents_processed = True

            # Save to project
            file_names = [pdf.name for pdf in pdf_docs]
            self.project_manager.save_files_to_project(
                st.session_state.current_project_id, pdf_docs, file_names
            )

            st.success("Documents processed successfully!")
            st.rerun()

    def handle_user_input(self, user_question):
        """Handle user question."""
        response = self.chat_service.handle_user_question(
            user_question, st.session_state.conversation
        )

        if response:
            st.session_state.chat_history = response["chat_history"]
            self.project_manager.save_session_to_project(
                st.session_state.current_project_id
            )

    def run(self):
        """Run the application."""
        self.setup_app()

        # Create default project if needed
        if not self.project_manager.get_all_projects():
            default_id = self.project_manager.create_project("My First Project", "📚")
            self.project_manager.set_current_project(default_id)

        # Header
        self.ui.render_header()

        # Project selector in main area
        self.ui.render_project_selector(self.project_manager)

        # Layout: sidebar and main content
        col1, col2 = st.columns([1, 3])

        with col1:
            sidebar_result = self.ui.render_sidebar(
                self.project_manager, self.chat_service
            )
            if sidebar_result and sidebar_result.get("action") == "process":
                self.process_documents(sidebar_result.get("files"))

        with col2:
            # Chat input
            user_input = self.ui.render_chat_input()
            if user_input:
                self.handle_user_input(user_input)

            # Chat or welcome
            if st.session_state.get("chat_history"):
                self.ui.render_chat_history(st.session_state.chat_history)
            else:
                self.ui.render_welcome()


def main():
    """Main entry point."""
    app = StudyBuddyApp()
    app.run()


if __name__ == "__main__":
    main()
