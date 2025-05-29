"""UI components for StudyBuddy Streamlit interface."""

import streamlit as st
import time
from typing import List, Optional

from .templates import CSS_STYLES, BOT_MESSAGE_TEMPLATE, USER_MESSAGE_TEMPLATE


class UIComponents:
    """Handles UI components and rendering for StudyBuddy."""

    @staticmethod
    def render_header():
        """Render the main application header."""
        st.markdown(
            """
        <div class="main-header">
            <h1>🤖 StudyBuddy</h1>
            <p>Your AI-Powered Document Chat Assistant</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_status_indicator(has_conversation: bool):
        """Render status indicator based on conversation state."""
        if not has_conversation:
            st.markdown(
                """
            <div class="status-indicator status-error">
                ❌ No documents processed - Please upload and process documents first
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
            <div class="status-indicator status-ready">
                ✅ Ready to chat - Documents processed successfully
            </div>
            """,
                unsafe_allow_html=True,
            )

    @staticmethod
    def render_welcome_screen():
        """Render welcome screen with getting started instructions."""
        st.markdown(
            """
        <div class="welcome-screen">
            <h3>🎯 How to get started:</h3>
            <div class="feature-grid">
                <div class="feature-card">
                    <div class="feature-icon">📁</div>
                    <h4>1. Upload Documents</h4>
                    <p>Upload your PDF files using the sidebar. Multiple files are supported!</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⚡</div>
                    <h4>2. Process Documents</h4>
                    <p>Click "Process Documents" to analyze and index your content.</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">💬</div>
                    <h4>3. Start Chatting</h4>
                    <p>Ask questions about your documents and get AI-powered answers!</p>
                </div>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

    @staticmethod
    def render_chat_history(chat_history):
        """Render chat history with messages."""
        if chat_history:
            chat_container = st.container()
            with chat_container:
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

    @staticmethod
    def render_file_upload_section():
        """Render file upload section in sidebar."""
        st.header("📁 Upload Documents")

        pdf_docs = st.file_uploader(
            "Choose PDF files",
            accept_multiple_files=True,
            type=["pdf"],
            help="Upload one or more PDF documents to chat with",
        )

        if pdf_docs:
            st.info(f"📊 {len(pdf_docs)} file(s) selected")

            # Show file details
            with st.expander("📋 File Details"):
                for i, pdf in enumerate(pdf_docs, 1):
                    st.write(f"{i}. {pdf.name} ({pdf.size:,} bytes)")

        return pdf_docs

    @staticmethod
    def render_processing_progress(step: str, progress: int):
        """Render processing progress with status updates."""
        progress_bar = st.progress(progress)
        status_text = st.text(step)
        return progress_bar, status_text

    @staticmethod
    def render_sidebar_help():
        """Render help section in sidebar."""
        st.divider()
        st.subheader("ℹ️ Tips")
        st.markdown(
            """
        **Best Practices:**
        - Upload clear, text-based PDFs
        - Ask specific questions
        - Use follow-up questions for clarity
        - Try different phrasings if needed
        """
        )

        st.subheader("🆘 Need Help?")
        with st.expander("Common Issues"):
            st.markdown(
                """
            **PDF not working?**
            - Ensure PDF contains selectable text
            - Scanned images need OCR (not supported)
            
            **No response?**
            - Check your OpenAI API key
            - Verify internet connection
            
            **Poor answers?**
            - Ask more specific questions
            - Include context in your query
            """
            )

    @staticmethod
    def render_document_stats(document_count: Optional[int]):
        """Render document statistics."""
        if document_count:
            st.metric("📄 Documents Processed", document_count)

        if st.session_state.get("conversation"):
            st.success("✅ Documents ready for chat!")
