# ⚖️ Legal Analyzer LexPro

An AI-powered Legal Document Intelligence Assistant that helps law firms and legal professionals extract key information from legal texts, contracts, and court files using large language models like Mistral or LLaMA2.

---

## ✨ Features

- 📥 Upload `.pdf`, `.txt`, or paste legal text
- 🧠 Analyze using LLMs via [Ollama](https://ollama.com/)
- 📄 Auto-generate case summaries
- 📌 Extract key legal clauses (termination, liability, jurisdiction, etc.)
- 🔍 Identify named entities (people, dates, organizations, laws)
- 📤 Export results as `.txt` or `.json`
- 🎛 Switch between models (e.g., `mistral`, `llama2`)

---
## 🛠️ Tech Stack

- **Backend:** FastAPI — high-performance web framework for Python  
- **Frontend:** Streamlit — easy-to-build, interactive data apps  
- **LLM Integration:** Ollama — local large language model serving  
- **PDF Processing:** PyMuPDF (fitz) — extract text from PDF documents  
- **HTTP Requests:** requests — communicate between frontend and backend  
- **Deployment:** Uvicorn ASGI server for backend  

---
## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/legal-analyzer-lexpro.git
cd legal-analyzer-lexpro
```

2.  **Install Python Dependencies:**
    It's recommended to create a virtual environment first:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```
    Then, install the required libraries:
    ```bash
    pip install streamlit fastapi uvicorn PyMuPDF requests
    ```
    *(For a production setup, you might want to create separate `requirements.txt` files for `backend` and `frontend`.)*

    ### Running the Application

1.  **Start the Backend API:**
    Navigate to the `backend` directory:
    ```bash
    cd backend
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```
    This will start the FastAPI server, usually accessible at `http://localhost:8000`.

2.  **Start the Frontend Application:**
    Open a *new* terminal, navigate to the `frontend` directory:
    ```bash
    cd frontend
    streamlit run app.py
    ```
    This will open the Streamlit application in your web browser (typically at `http://localhost:8501`).
