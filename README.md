# Study Buddy

A minimalist AI-powered study assistant that helps you learn from your documents through simple conversation.

## What is Study Buddy?

Study Buddy is a simple application that helps you study more effectively. Upload your PDF study materials, and ask questions about them in plain language. The AI assistant will provide clear, helpful answers based on your documents.

## Features

- **Ask Questions About Your Documents**: Upload PDFs and get instant answers
- **Multiple Projects**: Organize different subjects into separate projects
- **Conversation Memory**: Ask follow-up questions naturally
- **Simple Mode**: Get study help even without uploading documents

## Getting Started

1. **Install dependencies**:

   ```bash
   pip install -r Requirements.txt
   ```

2. **Set up your API key**:

   - Copy `.env.example` to `.env`
   - Add your API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_key_here
     ```

3. **Start the app**:

   ```bash
   streamlit run main.py
   ```

## How to Use

### Create a Project

1. Enter a name like "Biology 101" or "Chemistry Notes"
2. Choose an icon
3. Click "Create Project"

### Add Documents

1. Upload your PDF files
2. Click "Process Documents"

### Start Learning

1. Type your question
2. Get an answer based on your documents
3. Ask follow-up questions

### Simple Mode

Toggle "Simple Chatbot Mode" to get general study help without documents.

## Troubleshooting

- **API Key Error**: Check your `.env` file has the correct API key
- **PDF Problems**: Make sure your PDFs aren't password-protected
- **Large Documents**: Very large PDFs might take longer to process
