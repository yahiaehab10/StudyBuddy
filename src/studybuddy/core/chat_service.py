"""Chat service for handling conversations with documents."""

from typing import Optional
import streamlit as st
from langchain_openai import ChatOpenAI  # Updated import
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from ..config.settings import settings


class ChatService:
    """Handles chat functionality and conversation management."""

    def __init__(self):
        self.llm = ChatOpenAI(**settings.get_llm_config())  # Now using updated class
        self.conversation = None

    def create_conversation_chain(
        self, vector_store: FAISS
    ) -> Optional[ConversationalRetrievalChain]:
        """Create conversation chain from vector store.

        Args:
            vector_store: FAISS vector store containing document embeddings

        Returns:
            Conversation chain or None if error occurs
        """
        try:
            conversation_chain = ConversationalRetrievalChain.from_llm(
                llm=self.llm,
                retriever=vector_store.as_retriever(),
                memory=ConversationBufferMemory(
                    memory_key="chat_history", return_messages=True
                ),
            )
            return conversation_chain
        except Exception as e:
            st.error(f"Error creating conversation chain: {str(e)}")
            return None

    def handle_user_question(self, question: str, conversation_chain) -> Optional[dict]:
        """Process user question and get response.

        Args:
            question: User's question
            conversation_chain: Active conversation chain

        Returns:
            Response dictionary with chat history or None if error
        """
        if not conversation_chain:
            st.error("🚫 Please upload and process documents first!")
            return None

        try:
            with st.spinner("🤔 StudyBuddy is thinking..."):
                # Use invoke instead of deprecated __call__
                response = conversation_chain.invoke({"question": question})
                return response
        except Exception as e:
            st.error(f"❌ Error processing your question: {str(e)}")
            return None

    def initialize_session_state(self):
        """Initialize Streamlit session state variables."""
        if "conversation" not in st.session_state:
            st.session_state.conversation = None
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = None
        if "documents_processed" not in st.session_state:
            st.session_state.documents_processed = False
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = []
        if "file_names" not in st.session_state:
            st.session_state.file_names = []
