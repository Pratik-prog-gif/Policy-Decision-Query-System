#  Policy Decision Query System

A FastAPI-based intelligent query system that analyzes **policy documents** (PDFs, DOCX, Emails) using **LLMs** and **semantic search**. It answers queries like **approval status**, **amount**, and **justification**, based on content in the uploaded document.

---

##  Features

-  Ingests **PDF**, **DOCX**, and **Email (EML, MSG)** files for analysis  
-  Performs **semantic search** using **HuggingFace embeddings** and **FAISS**  
-  Uses **OpenAI-compatible LLMs** (via **Groq**, e.g., LLaMA 3.3 70B) to reason over context  
-  Returns structured **JSON** with **decision**, **amount**, and **matched clauses**  
-  Secured via **`.env` variables** for API key handling  
-  Interactive API via **Swagger UI**

---

## Swagger UI Screenshots

###  File Upload Endpoint

_Use this endpoint to upload a policy document (PDF, DOCX, or EML)._

📷 _Insert screenshot here_  
`![Swagger Upload Screenshot](images/swagger_upload.png)`

---

### Query Endpoint

_After uploading, use this to query the document with a policy-related question._

📷 _Insert screenshot here_  
`![Swagger Query Screenshot](images/swagger_query.png)`

---

## Tech Stack

| Component          | Technology                                     |
|-------------------|------------------------------------------------|
| Backend Framework  | FastAPI                                        |
| LLM                | LLaMA 3.3 70B via Groq API                     |
| Vector Store       | FAISS                                          |
| Embeddings         | sentence-transformers/all-MiniLM-L6-v2        |
| Document Parsing   | LangChain Loaders (PDF, Word, Email)          |
| API Testing        | Swagger UI (FastAPI auto-docs)                |

---

##  Setup Instruction
 1. **Clone the repository:**
   ```bash
   git clone https://github.com/Pratik-prog-gif/Policy-Decision-Query-System.git
   cd policy-decision-query-system

   exit

   




