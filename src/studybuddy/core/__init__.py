"""Core package initialization."""

from .document_processor import DocumentProcessor
from .chat_service import ChatService
from .project_manager import ProjectManager
from .peft_service import PEFTNoteTakingService

__all__ = [
    "DocumentProcessor",
    "ChatService",
    "ProjectManager",
    "PEFTNoteTakingService",
]
