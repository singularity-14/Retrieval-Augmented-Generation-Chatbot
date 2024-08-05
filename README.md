# Retrieval Augmented Generation (RAG) Chatbot with PDF Processing

This project is a Retrieval-Augmented Generation (RAG) chatbot application using Streamlit that processes PDF files, extracts and chunks text, uploads it to a vector database, and utilizes a language model to answer questions based on the uploaded pdf content.

## Features

- The PDF processing uses PyMuPDF to extract text from PDF files.
- Text chunking is performed using RecursiveCharacterTextSplitter.
- Vector storage and retrieval are handled using FAISS.
- The language model used for generating responses is Gemini-1.5-flash from Google.
- The application supports up to 3 PDF file uploads at a time.
