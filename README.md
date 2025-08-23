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



### Query Endpoint


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
   ```
2. **Install Dependecies:**
```bash
 pip install -r requirements.txt
```
 3. **Add API_KEY:**
```bash
   API_KEY=your_groq_api_key
```

4. **Run the FastAPI server:**
```bash
 uvicorn main:app --host 0.0.0.0 --port 8000
```
 5. **Access Swagger UI**
    ```bash
     http://localhost:8000/docs
   ```


