"""Configuration settings for StudyBuddy application."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    """Application settings and configuration."""

    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    # LLM Configuration
    LLM_MODEL = "gpt-3.5-turbo"
    LLM_TEMPERATURE = 0.7

    # Text Processing
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    TEXT_SEPARATOR = "\n"

    # Streamlit Configuration
    PAGE_TITLE = "StudyBuddy - AI Document Assistant"
    PAGE_ICON = "🤖"
    LAYOUT = "wide"

    # File Upload
    ALLOWED_FILE_TYPES = ["pdf"]
    MAX_FILE_SIZE_MB = 200

    @classmethod
    def validate_api_key(cls) -> bool:
        """Validate that OpenAI API key is set."""
        return bool(cls.OPENAI_API_KEY)

    @classmethod
    def get_text_splitter_config(cls) -> dict:
        """Get text splitter configuration."""
        return {
            "separator": cls.TEXT_SEPARATOR,
            "chunk_size": cls.CHUNK_SIZE,
            "chunk_overlap": cls.CHUNK_OVERLAP,
            "length_function": len,
        }

    @classmethod
    def get_llm_config(cls) -> dict:
        """Get LLM configuration."""
        return {"temperature": cls.LLM_TEMPERATURE, "model_name": cls.LLM_MODEL}


# Global settings instance
settings = Settings()
