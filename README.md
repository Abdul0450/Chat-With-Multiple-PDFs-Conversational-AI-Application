# Chat-With-Multiple-PDFs-Conversational-AI-Application

Project Overview
Chat With Multiple PDFs is a Python-based application designed to help users interact with PDF documents using AI technologies. The project uses Streamlit for the user interface, LangChain for text processing and conversational retrieval, Hugging Face Instructor XL for generating text embeddings, FAISS for vector storage and similarity search, and Ollama for local Large Language Model (LLM) integration.
The application extracts text from uploaded PDF files, divides the content into smaller chunks, generates vector embeddings, and creates a FAISS vector store to support a Retrieval-Augmented Generation (RAG) workflow.
Features
- Upload multiple PDF documents.
- Extract text from PDF pages using PyPDF2.
- Split text into chunks with configurable overlap.
- Generate embeddings using the Hugging Face Instructor XL model.
- Store document embeddings using FAISS.
- Integrate a local language model using Ollama.
- Use LangChain components to build a conversational retrieval pipeline.
- Provide an interactive web interface using Streamlit.
Technologies Used
- Python
- Streamlit
- LangChain
- PyPDF2
- Hugging Face Instructor XL
- FAISS
- Ollama
- python-dotenv
Application Workflow
1. Upload one or more PDF documents.
2. Extract text from the uploaded PDFs.
3. Split the extracted text into chunks of 1,000 characters with 200 characters of overlap.
4. Generate vector embeddings for the text chunks.
5. Create a FAISS vector store for similarity search.
6. Retrieve relevant document passages based on user questions once the retrieval workflow is connected.
7. Generate contextual answers using an LLM once the conversational chain is completed.
