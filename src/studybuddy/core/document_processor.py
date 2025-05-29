"""Document processing utilities for StudyBuddy."""

from typing import List, Optional
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings  # Updated import
from langchain_community.vectorstores import FAISS

from ..config.settings import settings


class DocumentProcessor:
    """Handles PDF document processing and text extraction."""

    def __init__(self):
        self.text_splitter = CharacterTextSplitter(
            **settings.get_text_splitter_config()
        )
        self.embeddings = OpenAIEmbeddings()  # Now using updated class

    def extract_text_from_pdfs(self, pdf_docs) -> Optional[str]:
        """Extract text from uploaded PDF documents.

        Args:
            pdf_docs: List of uploaded PDF files from Streamlit

        Returns:
            Concatenated text from all PDFs or None if error occurs
        """
        text = ""
        for pdf in pdf_docs:
            try:
                reader = PdfReader(pdf)
                for page in reader.pages:
                    text += page.extract_text() + "\n"
            except Exception as e:
                st.error(f"Error reading PDF {pdf.name}: {str(e)}")
                return None
        return text

    def split_text_into_chunks(self, raw_text: str) -> List[str]:
        """Split raw text into manageable chunks.

        Args:
            raw_text: Raw text extracted from documents

        Returns:
            List of text chunks
        """
        return self.text_splitter.split_text(raw_text)

    def create_vector_store(self, text_chunks: List[str]) -> Optional[FAISS]:
        """Create FAISS vector store from text chunks.

        Args:
            text_chunks: List of text chunks

        Returns:
            FAISS vector store or None if error occurs
        """
        try:
            vector_store = FAISS.from_texts(text_chunks, self.embeddings)
            return vector_store
        except Exception as e:
            st.error(f"Error creating vector store: {str(e)}")
            return None

    def process_documents(self, pdf_docs) -> Optional[FAISS]:
        """Complete document processing pipeline.

        Args:
            pdf_docs: List of uploaded PDF files

        Returns:
            FAISS vector store ready for querying or None if error
        """
        # Extract text
        raw_text = self.extract_text_from_pdfs(pdf_docs)
        if raw_text is None:
            return None

        if not raw_text.strip():
            st.error("❌ No text found in PDFs")
            return None

        # Split into chunks
        text_chunks = self.split_text_into_chunks(raw_text)

        # Create vector store
        vector_store = self.create_vector_store(text_chunks)
        return vector_store
