# Study Buddy - AI-Powered Study Assistant

Study Buddy is a clean, simple Streamlit application that helps you study more effectively by allowing you to upload PDF documents and chat with an AI assistant about their content.

## Features

- **Clean, Minimalist Interface**: Simple and intuitive design for distraction-free studying
- **Project Management**: Create and manage multiple study projects
- **Document Processing**: Upload and process multiple PDF documents
- **AI-Powered Q&A**: Ask questions about your documents in natural language
- **Smart Responses**: Get intelligent responses based on your documents
- **Simple Chatbot Mode**: Get study help even without uploading documents

## Setup

1. **Install dependencies:**

   ```bash
   pip install -r Requirements.txt
   ```

2. **Set up environment variables:**

   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your_actual_api_key_here
     ```

3. **Run the application:**
   ```bash
   streamlit run main.py
   ```

## Usage

1. **Create a Project**: Create a new study project (e.g., "Physics 101")
2. **Upload Documents**: Upload one or more PDF study materials
3. **Process Documents**: Click "Process Documents" to extract and analyze content
4. **Ask Questions**: Type your study questions in the chat input
5. **Get Answers**: Receive clear, helpful answers based on your documents

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls

## Troubleshooting

- **"Please set your OPENAI_API_KEY"**: Ensure you have a `.env` file with a valid OpenAI API key
- **PDF reading errors**: Check that your PDFs are not password-protected or corrupted
- **No text extracted**: Some PDFs might be image-based and require OCR (not currently supported)

## License

MIT License
