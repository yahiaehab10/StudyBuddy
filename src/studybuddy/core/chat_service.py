"""Chat service for handling conversations with documents."""

from typing import Optional
import streamlit as st
from langchain_openai import ChatOpenAI  # Updated import
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from ..config.settings import settings
from .peft_service import PEFTNoteTakingService


class ChatService:
    """Handles chat functionality and conversation management."""

    def __init__(self):
        self.llm = ChatOpenAI(**settings.get_llm_config())  # Now using updated class
        self.conversation = None
        self.peft_service = PEFTNoteTakingService()
        self.use_note_style = False

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
                # Check if we should use note-taking style
                if self.use_note_style and self.peft_service.is_initialized:
                    # Get relevant context from the retriever
                    retriever = conversation_chain.retriever
                    relevant_docs = retriever.get_relevant_documents(question)
                    context = "\n".join([doc.page_content for doc in relevant_docs[:2]])

                    # Generate note-style response
                    note_response = self.peft_service.generate_note_style_response(
                        question, context
                    )

                    # Create a mock response in the expected format
                    from langchain.schema import HumanMessage, AIMessage

                    # Get existing chat history
                    memory = conversation_chain.memory
                    chat_history = memory.chat_memory.messages.copy()

                    # Add new messages
                    chat_history.append(HumanMessage(content=question))
                    chat_history.append(AIMessage(content=note_response))

                    # Update memory
                    memory.chat_memory.messages = chat_history

                    return {"chat_history": chat_history, "answer": note_response}
                else:
                    # Use normal LangChain response
                    response = conversation_chain.invoke({"question": question})
                    return response

        except Exception as e:
            st.error(f"❌ Error processing your question: {str(e)}")
            return None

    def toggle_note_style(self, enable: bool):
        """Toggle note-taking style responses."""
        self.use_note_style = enable

    def setup_peft_for_project(
        self, project_id: str, document_chunks: list = None
    ) -> bool:
        """Set up PEFT fine-tuning for a specific project."""
        try:
            # Try to load existing fine-tuned model
            if self.peft_service.load_fine_tuned_model(project_id):
                return True

            # Initialize the template-based system
            if not self.peft_service.initialize_model():
                return False

            # Prepare training data (for template system)
            custom_examples = []
            if document_chunks:
                custom_examples = (
                    self.peft_service.create_training_examples_from_documents(
                        document_chunks
                    )
                )

            training_data = self.peft_service.prepare_training_data(custom_examples)

            # Setup the template system
            if self.peft_service.fine_tune_model(training_data):
                # Save the configuration
                return self.peft_service.save_fine_tuned_model(project_id)

            return False

        except Exception as e:
            st.error(f"Error setting up note-taking style: {str(e)}")
            return False

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
        if "note_style_enabled" not in st.session_state:
            st.session_state.note_style_enabled = False
        if "peft_initialized" not in st.session_state:
            st.session_state.peft_initialized = False
