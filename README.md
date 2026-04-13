# 📑 RAG Chatbot with PDF Processing

> Upload your PDFs and chat with them — a Retrieval-Augmented Generation chatbot that extracts, chunks, and semantically indexes PDF content, then answers questions using Google Gemini 1.5 Flash.

---

## 📌 Project Overview

This application lets users **upload up to 3 PDF files** and ask natural language questions about their content. Rather than feeding entire documents into an LLM (which hits context limits), it uses a **RAG pipeline** — smartly chunking and indexing text into a FAISS vector store, retrieving only the most relevant passages, and generating precise, context-grounded answers via Gemini 1.5 Flash.

Built with a clean separation between frontend (`app.py`) and backend (`backend.py`) for maintainability.

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 📄 PDF text extraction | PyMuPDF extracts text page-by-page with source + page metadata |
| ✂️ Smart chunking | `RecursiveCharacterTextSplitter` (1000 chars, 20 overlap) for optimal retrieval |
| 🔍 Semantic search | FAISS vector store with HuggingFace BGE embeddings |
| 🤖 Grounded answers | Gemini 1.5 Flash responds strictly within document context |
| 🚫 Hallucination guard | Prompt-engineered to respond "I don't know" when answer isn't in context |
| 💬 Chat history | Full conversation stored in Streamlit session state |
| 📁 Multi-PDF support | Handles up to 3 PDFs simultaneously in one session |

---

## 🚀 Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| LLM | Google Gemini 1.5 Flash |
| RAG Framework | LangChain (LCEL — Runnable chain) |
| Vector Database | FAISS (persisted locally) |
| Embeddings | HuggingFace BGE Embeddings (open-source) |
| PDF Processing | PyMuPDF (`fitz`) |
| Frontend | Streamlit |
| Config | python-dotenv |

---

## 🏗️ Architecture

```
User uploads PDF(s) (max 3)
        ↓
PyMuPDF → page-by-page text extraction
  └── Metadata: source filename + page number
        ↓
RecursiveCharacterTextSplitter
  └── chunk_size=1000, chunk_overlap=20
        ↓
HuggingFace BGE Embeddings → FAISS Vector Store
  └── Persisted to: vector_store_of_recently_uploaded_pdfs/
        ↓
User asks a question
        ↓
FAISS Retriever → top-k relevant chunks
        ↓
LangChain LCEL Chain:
  {context: retriever, question: passthrough}
  → ChatPromptTemplate
  → Gemini 1.5 Flash
  → StrOutputParser
        ↓
Answer displayed in Streamlit chat UI
```

---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/rag-pdf-chatbot.git
cd rag-pdf-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file in the project root:
```bash
GOOGLE_API_KEY=your_google_api_key_here
```
> Get your key at [aistudio.google.com](https://aistudio.google.com)

### 4. Run the app
```bash
streamlit run app.py
```
Visit `http://localhost:8501` in your browser.

---

## 🖥️ How to Use

1. **Upload PDFs** — use the sidebar uploader (up to 3 files)
2. **Click Submit** — triggers extraction, chunking, and FAISS indexing
3. **Ask questions** — type in the chat input and get context-grounded answers
4. **Follow up** — full chat history is preserved within the session

---

## 📂 Project Structure

```
rag-pdf-chatbot/
│
├── app.py                                       # Streamlit UI — upload, chat interface, session state
├── backend.py                                   # Core pipeline — PDF extraction, chunking, FAISS, LLM chain
├── requirements.txt                             # Python dependencies
├── .env                                         # API keys (not committed to version control)
├── vector_store_of_recently_uploaded_pdfs/      # Persisted FAISS index (auto-generated)
└── README.md                                    # Project documentation
```

---

## 💡 Key Learnings & Takeaways

- Built a **full RAG pipeline** using LangChain's LCEL (LangChain Expression Language) for composable, readable chain construction
- Used **page-level metadata** (source + page number) during PDF extraction for traceable, auditable retrieval
- Applied **prompt engineering** to prevent hallucinations — model explicitly instructed to stay within retrieved context
- Chose **open-source BGE embeddings** over paid APIs, keeping the pipeline cost-efficient
- Implemented **local FAISS persistence** so the vector store survives app restarts without re-processing

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

*Demonstrating end-to-end RAG pipeline design with document ingestion, semantic retrieval, and grounded LLM response generation.*
