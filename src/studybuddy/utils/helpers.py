"""Utility functions for StudyBuddy application."""

import streamlit as st
from typing import Any, Dict


def validate_environment() -> bool:
    """Validate that required environment variables are set.

    Returns:
        True if environment is valid, False otherwise
    """
    from ..config.settings import settings

    if not settings.validate_api_key():
        st.error("🔑 Please set your OPENAI_API_KEY in a .env file")
        st.info("💡 Create a .env file with: OPENAI_API_KEY=your_api_key_here")
        return False
    return True


def initialize_streamlit_config():
    """Initialize Streamlit page configuration."""
    from ..config.settings import settings

    st.set_page_config(
        page_title=settings.PAGE_TITLE,
        page_icon=settings.PAGE_ICON,
        layout=settings.LAYOUT,
        initial_sidebar_state="expanded",
    )


def clear_chat_session():
    """Clear the current chat session and reset state."""
    st.session_state.conversation = None
    st.session_state.chat_history = None
    st.session_state.documents_processed = False
    if "document_count" in st.session_state:
        del st.session_state.document_count


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Formatted size string
    """
    if size_bytes == 0:
        return "0B"

    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1

    return f"{size_bytes:.1f}{size_names[i]}"


def get_session_state_summary() -> Dict[str, Any]:
    """Get summary of current session state for debugging.

    Returns:
        Dictionary with session state information
    """
    return {
        "has_conversation": st.session_state.get("conversation") is not None,
        "has_chat_history": st.session_state.get("chat_history") is not None,
        "documents_processed": st.session_state.get("documents_processed", False),
        "document_count": st.session_state.get("document_count", 0),
    }
