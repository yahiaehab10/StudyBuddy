"""Main application file for StudyBuddy - Structured version."""

import streamlit as st
import time

# Import our structured modules
from src.studybuddy.config.settings import settings
from src.studybuddy.core.document_processor import DocumentProcessor
from src.studybuddy.core.chat_service import ChatService
from src.studybuddy.ui.components import UIComponents
from src.studybuddy.ui.templates import CSS_STYLES
from src.studybuddy.utils.helpers import (
    validate_environment,
    initialize_streamlit_config,
    clear_chat_session,
)


class StudyBuddyApp:
    """Main application class for StudyBuddy."""

    def __init__(self):
        self.document_processor = DocumentProcessor()
        self.chat_service = ChatService()
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
        if not user_question.strip():
            return

        response = self.chat_service.handle_user_question(
            user_question, st.session_state.conversation
        )

        if response:
            st.session_state.chat_history = response["chat_history"]
            # Don't try to clear the input - let Streamlit handle it naturally

    def process_documents(self, pdf_docs):
        """Process uploaded PDF documents."""
        if not pdf_docs:
            st.warning("⚠️ Please upload at least one PDF document.")
            return

        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            # Step 1: Process documents
            status_text.text("📖 Extracting text from PDFs...")
            progress_bar.progress(25)

            vector_store = self.document_processor.process_documents(pdf_docs)
            if vector_store is None:
                return

            # Step 2: Create conversation chain
            status_text.text("🔗 Setting up conversation chain...")
            progress_bar.progress(75)

            conversation = self.chat_service.create_conversation_chain(vector_store)
            if conversation is None:
                return

            # Step 3: Complete setup
            progress_bar.progress(100)
            st.session_state.conversation = conversation
            st.session_state.documents_processed = True
            st.session_state.document_count = len(pdf_docs)

            status_text.text("✅ Processing complete!")
            time.sleep(1)

            st.success(
                "🎉 Documents processed successfully! You can now ask questions."
            )
            st.balloons()

        except Exception as e:
            st.error(f"❌ Error during processing: {str(e)}")
        finally:
            progress_bar.empty()
            status_text.empty()

    def render_main_content(self):
        """Render the main content area."""
        col1, col2 = st.columns([3, 1])

        with col1:
            # Status indicator
            self.ui.render_status_indicator(st.session_state.conversation is not None)

            # Chat input with send button
            st.subheader("💬 Chat with your documents")

            # Create input columns
            input_col1, input_col2 = st.columns([4, 1])

            with input_col1:
                user_question = st.text_input(
                    "Ask a question about your documents:",
                    placeholder="e.g., What are the main topics discussed in the document?",
                    key="user_input",
                )

            with input_col2:
                st.markdown(
                    "<div style='padding-top: 1.8rem;'>", unsafe_allow_html=True
                )
                send_button = st.button(
                    "Send", type="primary", use_container_width=True
                )
                st.markdown("</div>", unsafe_allow_html=True)

            # Handle input from either text input or send button
            if user_question or send_button:
                if st.session_state.user_input.strip():
                    self.handle_user_input(st.session_state.user_input)

            # Render chat history or welcome screen
            if st.session_state.chat_history:
                self.ui.render_chat_history(st.session_state.chat_history)
            else:
                self.ui.render_welcome_screen()

        with col2:
            # Document statistics
            st.subheader("📚 Document Management")
            self.ui.render_document_stats(st.session_state.get("document_count"))

    def render_sidebar(self):
        """Render the sidebar with file upload and controls."""
        with st.sidebar:
            # File upload section
            pdf_docs = self.ui.render_file_upload_section()

            # Process button
            process_button = st.button(
                "🚀 Process Documents", type="primary", use_container_width=True
            )

            if process_button:
                self.process_documents(pdf_docs)

            # Clear session button
            if st.session_state.conversation:
                st.divider()
                if st.button(
                    "🗑️ Clear Session", help="Clear current session and start over"
                ):
                    clear_chat_session()
                    st.rerun()

            # Help section
            self.ui.render_sidebar_help()

    def run(self):
        """Run the main application."""
        # Setup
        self.setup_app()

        # Render header
        self.ui.render_header()

        # Render main content
        self.render_main_content()

        # Render sidebar
        self.render_sidebar()


def main():
    """Main entry point for the application."""
    app = StudyBuddyApp()
    app.run()


if __name__ == "__main__":
    main()
