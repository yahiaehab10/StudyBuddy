"""Main application file for StudyBuddy - Minimalist version."""

import streamlit as st
import time

# Import our structured modules
from src.studybuddy.config.settings import settings
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
    """Main application class for StudyBuddy."""

    def __init__(self):
        self.document_processor = DocumentProcessor()
        self.chat_service = ChatService()
        self.project_manager = ProjectManager()
        self.ui = UIComponents()

    def setup_app(self):
        """Setup the Streamlit application."""
        initialize_streamlit_config()

        # Validate environment
        if not validate_environment():
            st.stop()

        # Apply CSS styles
        st.write(CSS_STYLES, unsafe_allow_html=True)

        # Initialize session state
        self.chat_service.initialize_session_state()

    def handle_user_input(self, user_question: str):
        """Handle user question input and generate response."""
        response = self.chat_service.handle_user_question(
            user_question, st.session_state.conversation
        )

        if response:
            st.session_state.chat_history = response["chat_history"]
            self.project_manager.save_session_to_project(
                st.session_state.current_project_id
            )

    def process_documents(self, pdf_docs):
        """Process uploaded PDF documents with minimal UI feedback."""
        if not pdf_docs:
            st.warning("Please upload at least one PDF document.")
            return

        # Save files to current project
        file_names = [pdf.name for pdf in pdf_docs]
        self.project_manager.save_files_to_project(
            st.session_state.current_project_id, pdf_docs, file_names
        )

        with st.spinner("Processing documents..."):
            # Process documents
            vector_store = self.document_processor.process_documents(pdf_docs)
            if vector_store is None:
                return

            # Create conversation chain
            conversation = self.chat_service.create_conversation_chain(vector_store)
            if conversation is None:
                return

            # Update session state
            st.session_state.conversation = conversation
            st.session_state.documents_processed = True
            st.session_state.document_count = len(pdf_docs)
            st.session_state.uploaded_files = pdf_docs
            st.session_state.file_names = file_names

            # Save to project
            self.project_manager.save_session_to_project(
                st.session_state.current_project_id
            )

            st.success("Documents processed successfully!")
            time.sleep(1)
            st.rerun()

    def run(self):
        """Run the main application with clean layout."""
        # Setup
        self.setup_app()

        # Header
        self.ui.render_header()

        # Create default project if none exist
        if not self.project_manager.get_all_projects():
            default_id = self.project_manager.create_project(
                name="My First Project",
                emoji="📚",
            )
            self.project_manager.set_current_project(default_id)

        # Main layout: sidebar and main content
        with st.sidebar:
            pdf_docs = self.ui.render_sidebar_content(self.project_manager)
            if pdf_docs:
                self.process_documents(pdf_docs)

        # Main content area
        user_input = self.ui.render_main_chat_area(self.project_manager)
        if user_input:
            self.handle_user_input(user_input)

        # Chat history or welcome
        if st.session_state.chat_history:
            self.ui.render_chat_history(st.session_state.chat_history)
        else:
            self.ui.render_welcome_screen()

        # Project stats in a clean sidebar section
        with st.sidebar:
            st.divider()
            self.ui.render_project_stats(self.project_manager)


def main():
    """Main entry point for the application."""
    app = StudyBuddyApp()
    app.run()


if __name__ == "__main__":
    main()
