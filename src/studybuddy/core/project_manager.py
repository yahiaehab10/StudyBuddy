"""Project manager for handling multiple subjects/projects in StudyBuddy."""

from typing import Dict, List, Optional, Any
import streamlit as st
from datetime import datetime
import uuid

from ..config.settings import settings


class ProjectManager:
    """Manages multiple projects/subjects for students."""

    def __init__(self):
        self.initialize_projects_session_state()

    def initialize_projects_session_state(self):
        """Initialize project-related session state variables."""
        if "projects" not in st.session_state:
            st.session_state.projects = {}
        if "current_project_id" not in st.session_state:
            st.session_state.current_project_id = None
        if "project_selector_key" not in st.session_state:
            st.session_state.project_selector_key = 0

    def create_project(
        self, name: str, emoji: str = None, description: str = ""
    ) -> str:
        """Create a new project.

        Args:
            name: Project name
            emoji: Project emoji (optional)
            description: Project description (optional)

        Returns:
            Project ID
        """
        project_id = str(uuid.uuid4())[:8]

        if not emoji:
            emoji = settings.DEFAULT_PROJECT_EMOJI

        project = {
            "id": project_id,
            "name": name,
            "emoji": emoji,
            "description": description,
            "created_at": datetime.now().isoformat(),
            "document_count": 0,
            "uploaded_files": [],  # Store uploaded PDF files
            "file_names": [],  # Store file names for display
            "conversation": None,
            "chat_history": None,
            "vector_store": None,
        }

        st.session_state.projects[project_id] = project
        return project_id

    def get_project(self, project_id: str) -> Optional[Dict[str, Any]]:
        """Get project by ID."""
        return st.session_state.projects.get(project_id)

    def get_all_projects(self) -> Dict[str, Dict[str, Any]]:
        """Get all projects."""
        return st.session_state.projects

    def delete_project(self, project_id: str) -> bool:
        """Delete a project.

        Args:
            project_id: Project ID to delete

        Returns:
            True if deleted, False if not found
        """
        if project_id in st.session_state.projects:
            del st.session_state.projects[project_id]

            # If this was the current project, clear current project
            if st.session_state.current_project_id == project_id:
                st.session_state.current_project_id = None
                self.clear_current_session_data()

            return True
        return False

    def set_current_project(self, project_id: str):
        """Set the current active project."""
        if project_id in st.session_state.projects:
            # Save current session data to the old project
            if st.session_state.current_project_id:
                self.save_session_to_project(st.session_state.current_project_id)

            # Switch to new project
            st.session_state.current_project_id = project_id
            self.load_project_to_session(project_id)

    def get_current_project(self) -> Optional[Dict[str, Any]]:
        """Get the current active project."""
        if st.session_state.current_project_id:
            return self.get_project(st.session_state.current_project_id)
        return None

    def save_session_to_project(self, project_id: str):
        """Save current session data to a project."""
        if project_id in st.session_state.projects:
            project = st.session_state.projects[project_id]
            project["conversation"] = st.session_state.get("conversation")
            project["chat_history"] = st.session_state.get("chat_history")
            project["document_count"] = st.session_state.get("document_count", 0)
            project["documents_processed"] = st.session_state.get(
                "documents_processed", False
            )
            project["uploaded_files"] = st.session_state.get("uploaded_files", [])
            project["file_names"] = st.session_state.get("file_names", [])
            project["last_updated"] = datetime.now().isoformat()

    def load_project_to_session(self, project_id: str):
        """Load project data to current session."""
        if project_id in st.session_state.projects:
            project = st.session_state.projects[project_id]
            st.session_state.conversation = project.get("conversation")
            st.session_state.chat_history = project.get("chat_history")
            st.session_state.document_count = project.get("document_count", 0)
            st.session_state.documents_processed = project.get(
                "documents_processed", False
            )
            st.session_state.uploaded_files = project.get("uploaded_files", [])
            st.session_state.file_names = project.get("file_names", [])

    def clear_current_session_data(self):
        """Clear current session data."""
        st.session_state.conversation = None
        st.session_state.chat_history = None
        st.session_state.document_count = 0
        st.session_state.documents_processed = False
        st.session_state.uploaded_files = []
        st.session_state.file_names = []

    def clear_project_data(self, project_id: str):
        """Clear all data for a specific project."""
        if project_id in st.session_state.projects:
            project = st.session_state.projects[project_id]
            project["conversation"] = None
            project["chat_history"] = None
            project["document_count"] = 0
            project["documents_processed"] = False
            project["vector_store"] = None
            project["uploaded_files"] = []
            project["file_names"] = []

            # If this is the current project, also clear session
            if st.session_state.current_project_id == project_id:
                self.clear_current_session_data()

    def save_files_to_project(self, project_id: str, pdf_files, file_names):
        """Save uploaded files to a specific project."""
        if project_id in st.session_state.projects:
            project = st.session_state.projects[project_id]
            project["uploaded_files"] = pdf_files
            project["file_names"] = file_names
            project["document_count"] = len(pdf_files)

            # Also update session state if this is the current project
            if st.session_state.current_project_id == project_id:
                st.session_state.uploaded_files = pdf_files
                st.session_state.file_names = file_names
                st.session_state.document_count = len(pdf_files)

    def get_project_files(self, project_id: str):
        """Get uploaded files for a specific project."""
        if project_id in st.session_state.projects:
            project = st.session_state.projects[project_id]
            return project.get("uploaded_files", []), project.get("file_names", [])
        return [], []

    def get_project_list_for_selectbox(self) -> List[str]:
        """Get formatted project list for selectbox."""
        projects = []
        for project_id, project in st.session_state.projects.items():
            display_name = f"{project['emoji']} {project['name']}"
            projects.append(display_name)
        return projects

    def get_project_id_from_display_name(self, display_name: str) -> Optional[str]:
        """Get project ID from display name."""
        for project_id, project in st.session_state.projects.items():
            project_display = f"{project['emoji']} {project['name']}"
            if project_display == display_name:
                return project_id
        return None

    def get_projects_summary(self) -> Dict[str, int]:
        """Get summary statistics for all projects."""
        total_projects = len(st.session_state.projects)
        total_documents = sum(
            project.get("document_count", 0)
            for project in st.session_state.projects.values()
        )
        active_projects = sum(
            1
            for project in st.session_state.projects.values()
            if project.get("conversation") is not None
        )

        return {
            "total_projects": total_projects,
            "total_documents": total_documents,
            "active_projects": active_projects,
        }
