import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
    )
    text_chunks = text_splitter.split_text(raw_text)
    return text_chunks


def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(text_chunks, embeddings)
    return vector_store


def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(),
        memory=ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        ),
    )
    return conversation_chain


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize the Streamlit session state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    # Set up the Streamlit app configuration
    st.set_page_config(
        page_title="Study Buddy",
        page_icon=":books:",
    )

    # Streamlit app layout
    st.header("Welcome to Study Buddy! :books:")
    st.text_input("How can I help you?")

    with st.sidebar:
        st.subheader("Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here", accept_multiple_files=True)
        if st.button("Process Documents"):
            with st.spinner("Processing documents..."):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vector_store = get_vector_store(text_chunks)

                # conversation chain
                st.session_state.conversation = get_conversation_chain(vector_store)


if __name__ == "__main__":
    main()
