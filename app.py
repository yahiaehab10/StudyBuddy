import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
import time

from htmlTemplates import bot_template, user_template, css


def get_pdf_text(pdf_docs):
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


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    text_chunks = text_splitter.split_text(raw_text)
    return text_chunks


def get_vector_store(text_chunks):
    try:
        embeddings = OpenAIEmbeddings()
        vector_store = FAISS.from_texts(text_chunks, embeddings)
        return vector_store
    except Exception as e:
        st.error(f"Error creating vector store: {str(e)}")
        return None


def get_conversation_chain(vector_store):
    try:
        llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vector_store.as_retriever(),
            memory=ConversationBufferMemory(
                memory_key="chat_history", return_messages=True
            ),
        )
        return conversation_chain
    except Exception as e:
        st.error(f"Error creating conversation chain: {str(e)}")
        return None


def handle_user_input(user_question):
    if st.session_state.conversation is None:
        st.error("🚫 Please upload and process documents first!")
        return

    try:
        # Show typing indicator
        with st.spinner("🤔 StudyBuddy is thinking..."):
            response = st.session_state.conversation({"question": user_question})
            st.session_state.chat_history = response["chat_history"]

        # Display chat history in a container
        chat_container = st.container()
        with chat_container:
            st.markdown('<div class="chat-container">', unsafe_allow_html=True)
            for i, message in enumerate(st.session_state.chat_history):
                if i % 2 == 0:
                    st.write(
                        user_template.replace("{{MSG}}", message.content),
                        unsafe_allow_html=True,
                    )
                else:
                    st.write(
                        bot_template.replace("{{MSG}}", message.content),
                        unsafe_allow_html=True,
                    )
            st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error processing your question: {str(e)}")


def show_welcome_screen():
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


def show_status_indicator():
    if st.session_state.conversation is None:
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


def main():
    # Set up the Streamlit app configuration (must be first)
    st.set_page_config(
        page_title="StudyBuddy - AI Document Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Load environment variables from .env file
    load_dotenv()

    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        st.error("🔑 Please set your OPENAI_API_KEY in a .env file")
        st.info("💡 Create a .env file with: OPENAI_API_KEY=your_api_key_here")
        st.stop()

    st.write(css, unsafe_allow_html=True)

    # Initialize the Streamlit session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "documents_processed" not in st.session_state:
        st.session_state.documents_processed = False

    # Custom header
    st.markdown(
        """
    <div class="main-header">
        <h1>🤖 StudyBuddy</h1>
        <p>Your AI-Powered Document Chat Assistant</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Main content area
    col1, col2 = st.columns([3, 1])

    with col1:
        # Status indicator
        show_status_indicator()

        # Chat input
        st.subheader("💬 Chat with your documents")
        user_question = st.text_input(
            "Ask a question about your documents:",
            placeholder="e.g., What are the main topics discussed in the document?",
            key="user_input",
        )

        if user_question:
            handle_user_input(user_question)

        # Show welcome screen if no chat history
        if st.session_state.chat_history is None:
            show_welcome_screen()

    with col2:
        # Sidebar content in the right column for better layout
        st.subheader("📚 Document Management")

        # File upload statistics
        if st.session_state.conversation:
            st.success("✅ Documents ready for chat!")

        # Document count display
        if "document_count" in st.session_state:
            st.metric("📄 Documents Processed", st.session_state.document_count)

    # Sidebar
    with st.sidebar:
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

        process_button = st.button(
            "🚀 Process Documents", type="primary", use_container_width=True
        )

        if process_button:
            if not pdf_docs:
                st.warning("⚠️ Please upload at least one PDF document.")
            else:
                progress_bar = st.progress(0)
                status_text = st.empty()

                try:
                    # Step 1: Extract text
                    status_text.text("📖 Extracting text from PDFs...")
                    progress_bar.progress(25)

                    raw_text = get_pdf_text(pdf_docs)
                    if raw_text is None:
                        return

                    if not raw_text.strip():
                        st.error(
                            "❌ No text could be extracted from the uploaded PDFs."
                        )
                        return

                    # Step 2: Split text
                    status_text.text("✂️ Splitting text into chunks...")
                    progress_bar.progress(50)

                    text_chunks = get_text_chunks(raw_text)
                    st.session_state.document_count = len(pdf_docs)

                    # Step 3: Create embeddings
                    status_text.text("🧠 Creating embeddings...")
                    progress_bar.progress(75)

                    vector_store = get_vector_store(text_chunks)
                    if vector_store is None:
                        return

                    # Step 4: Setup conversation
                    status_text.text("🔗 Setting up conversation chain...")
                    progress_bar.progress(90)

                    conversation = get_conversation_chain(vector_store)
                    if conversation is None:
                        return

                    progress_bar.progress(100)
                    st.session_state.conversation = conversation
                    st.session_state.documents_processed = True

                    status_text.text("✅ Processing complete!")
                    time.sleep(1)

                    st.success(
                        "🎉 Documents processed successfully! You can now ask questions."
                    )
                    st.balloons()

                except Exception as e:
                    st.error(f"❌ Error during processing: {str(e)}")
                finally:
                    progress_bar.empty()
                    status_text.empty()

        # Additional info
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


if __name__ == "__main__":
    main()
