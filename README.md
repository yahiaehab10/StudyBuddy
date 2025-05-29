# StudyBuddy - AI-Powered Document Chat Assistant

StudyBuddy is a Streamlit-based application that allows you to upload PDF documents and chat with an AI assistant about their content using OpenAI's language models.

## Features

- Upload multiple PDF documents
- Extract and process text from PDFs
- Ask questions about your documents in natural language
- Get AI-powered responses based on document content
- Maintain conversation history
- Beautiful chat interface with user and bot avatars

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
   streamlit run app.py
   ```

## Usage

1. **Upload Documents**: Use the sidebar to upload one or more PDF files
2. **Process Documents**: Click "Process Documents" to extract and index the content
3. **Ask Questions**: Type your questions in the text input field
4. **Get Answers**: The AI will respond based on the content of your uploaded documents

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection for API calls

## Troubleshooting

- **"Please set your OPENAI_API_KEY"**: Make sure you have a `.env` file with a valid OpenAI API key
- **PDF reading errors**: Ensure your PDFs are not password-protected or corrupted
- **No text extracted**: Some PDFs might be image-based and require OCR (not currently supported)

## License

MIT License
