"""StudyBuddy - AI-Powered Document Chat Assistant.

A Streamlit application that allows users to upload PDF documents
and chat with them using OpenAI's language models.
"""

__version__ = "1.0.0"
__author__ = "StudyBuddy Team"

from .config.settings import settings
from .core.document_processor import DocumentProcessor
from .core.chat_service import ChatService
from .core.project_manager import ProjectManager
from .ui.components import UIComponents

__all__ = [
    "settings",
    "DocumentProcessor",
    "ChatService",
    "ProjectManager",
    "UIComponents",
]
