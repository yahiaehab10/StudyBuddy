"""Chat service for handling conversations with documents."""

from typing import Optional
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from ..config.settings import settings
from .peft_service import ChatbotService


class ChatService:
    """Handles chat functionality and conversation management."""

    def __init__(self):
        self.llm = ChatOpenAI(**settings.get_llm_config())
        self.conversation = None
        self.chatbot_service = ChatbotService()
        self.use_simple_chatbot = False

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
        try:
            with st.spinner("🤔 StudyBuddy is thinking..."):
                # Check if we should use simple chatbot mode
                if self.use_simple_chatbot or not conversation_chain:
                    # Get relevant context if available
                    context = ""
                    if conversation_chain:
                        retriever = conversation_chain.retriever
                        relevant_docs = retriever.get_relevant_documents(question)
                        context = "\n".join(
                            [doc.page_content for doc in relevant_docs[:2]]
                        )

                    # Generate chatbot response
                    chatbot_response = self.chatbot_service.generate_response(
                        question, context
                    )

                    # Create a mock response in the expected format
                    from langchain.schema import HumanMessage, AIMessage

                    # Get existing chat history if available
                    chat_history = []
                    if conversation_chain and conversation_chain.memory:
                        chat_history = (
                            conversation_chain.memory.chat_memory.messages.copy()
                        )

                    # Add new messages
                    chat_history.append(HumanMessage(content=question))
                    chat_history.append(AIMessage(content=chatbot_response))

                    # Update memory if available
                    if conversation_chain and conversation_chain.memory:
                        conversation_chain.memory.chat_memory.messages = chat_history

                    return {"chat_history": chat_history, "answer": chatbot_response}
                else:
                    # Use normal LangChain response with documents
                    response = conversation_chain.invoke({"question": question})
                    return response

        except Exception as e:
            st.error(f"❌ Error processing your question: {str(e)}")
            # Fallback to simple chatbot
            try:
                fallback_response = self.chatbot_service.generate_response(question, "")
                return {"chat_history": [], "answer": fallback_response}
            except:
                return None

    def toggle_simple_chatbot(self, enable: bool):
        """Toggle simple chatbot mode."""
        self.use_simple_chatbot = enable

    def get_study_tips(self) -> list:
        """Get study tips from the chatbot service."""
        return self.chatbot_service.get_study_tips()

    def search_knowledge_base(self, search_term: str) -> list:
        """Search the chatbot's knowledge base."""
        return self.chatbot_service.search_knowledge_base(search_term)

    def get_available_topics(self) -> list:
        """Get available topics from the chatbot."""
        return self.chatbot_service.get_available_topics()

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
        if "simple_chatbot_enabled" not in st.session_state:
            st.session_state.simple_chatbot_enabled = False
