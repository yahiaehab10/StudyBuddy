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
        llm = ChatOpenAI()
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
        st.error("Please upload and process documents first!")
        return

    try:
        response = st.session_state.conversation({"question": user_question})
        st.session_state.chat_history = response["chat_history"]

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
    except Exception as e:
        st.error(f"Error processing your question: {str(e)}")


def main():
    # Set up the Streamlit app configuration (must be first)
    st.set_page_config(
        page_title="Study Buddy",
        page_icon=":books:",
    )

    # Load environment variables from .env file
    load_dotenv()

    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        st.error("Please set your OPENAI_API_KEY in a .env file")
        st.stop()

    st.write(css, unsafe_allow_html=True)

    # Initialize the Streamlit session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Streamlit app layout
    st.header("Welcome to Study Buddy! :books:")

    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here", accept_multiple_files=True, type=["pdf"]
        )
        if st.button("Process Documents"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF document.")
            else:
                with st.spinner("Processing documents..."):
                    # get pdf text
                    raw_text = get_pdf_text(pdf_docs)
                    if raw_text is None:
                        return

                    if not raw_text.strip():
                        st.error("No text could be extracted from the uploaded PDFs.")
                        return

                    # get the text chunks
                    text_chunks = get_text_chunks(raw_text)

                    # create vector store
                    vector_store = get_vector_store(text_chunks)
                    if vector_store is None:
                        return

                    # conversation chain
                    conversation = get_conversation_chain(vector_store)
                    if conversation is None:
                        return

                    st.session_state.conversation = conversation
                    st.success(
                        "Documents processed successfully! You can now ask questions."
                    )


if __name__ == "__main__":
    main()
