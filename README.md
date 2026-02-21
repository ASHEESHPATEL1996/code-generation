# 📘 GenAI Code Documentation Generator

An AI-powered application that automatically generates high-quality documentation for codebases using Large Language Models (LLMs).

Upload Python files, a ZIP project, or a GitHub repository to instantly produce structured documentation, project overviews, and inline docstrings — safely and efficiently.

🌐 **Live Application:**
https://code-generation-asheeshpatel.streamlit.app/

---

## 🚀 Key Features

* 🧠 AI-generated documentation for entire projects
* 📄 Inline docstring generation for functions and classes
* 📦 Supports single files, ZIP uploads, and GitHub repositories
* 🏗️ Project-level overview generation
* 🛡️ AST-based semantic validation to preserve code behavior
* 🔁 Safe fallback to original code if validation fails
* ⚡ Persistent caching for faster repeated runs
* ⬇️ Download updated files or full documented project as ZIP
* ☁️ Fully deployed web application (no local setup required)

---

## 🧩 How It Works

1. **Input Sources**

   * Upload `.py` files
   * Upload ZIP project
   * Provide a public GitHub repository URL

2. **AI Processing**

   * Code is analyzed using an LLM
   * Documentation and docstrings are generated
   * Project overview is created

3. **Safety Layer**

   * AST validation ensures semantic equivalence
   * Prevents accidental code logic changes
   * Falls back to original code if unsafe output detected

4. **Output**

   * Updated code with inline documentation
   * Project overview
   * Downloadable files or full ZIP archive

---

## 🏗️ Architecture Overview

```
User → Streamlit UI → Processing Pipeline → LLM → AST Validation → Output
```

### Core Components

* **Frontend:** Streamlit interface
* **LLM Engine:** Generates documentation content
* **AST Processor:** Inserts docstrings safely into code
* **Validation Layer:** Ensures semantics are preserved
* **Cache Layer:** Reduces latency and API costs

---

## 🧰 Tech Stack

### 🧠 AI & NLP

* OpenAI-compatible LLMs
* Prompt engineering for code understanding

### 🐍 Backend

* Python
* AST (Abstract Syntax Tree) processing
* Modular pipeline architecture

### 🖥️ Interface

* Streamlit

### 🗄️ Storage & Performance

* Persistent cache (database-backed)
* External API inference

---

## 📦 Example Use Cases

* Document legacy or poorly documented codebases
* Improve developer onboarding
* Generate API documentation quickly
* Assist open-source maintainers
* Prepare projects for production readiness
* Educational tooling for programming courses

---

## ▶️ Local Setup (Optional)

### 1️⃣ Clone the repository

```bash
git clone https://github.com/ASHEESHPATEL1996/code-generation
cd code-generation
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key
NEON_DB_URL=your_database_url
```

### 5️⃣ Run locally

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🛡️ Safety & Reliability

This system is designed to avoid breaking code:

* AST comparison ensures semantic equivalence
* Only documentation is added — logic remains unchanged
* Strict validation mode available
* Original files preserved on failure

---

## 🌟 Why This Project Matters

This project demonstrates real-world GenAI engineering capabilities:

* Safe AI-assisted code transformation
* Production-style validation pipeline
* Scalable architecture for large repositories
* Cost-aware caching strategy
* End-to-end AI application development
* Cloud deployment readiness

---

## 🔮 What’s Next

### 🔹 Function-by-Function Documentation Generation

Move from file-level documentation to fine-grained analysis:

* Detect individual functions and classes automatically
* Generate precise docstrings per function
* Improve accuracy for large and complex files
* Support selective regeneration for modified functions
* Provide richer input/output descriptions and usage examples

---

### 🔹 Intelligent Detection & Improvement

Enhance documentation quality through deeper analysis:

* Detect missing or low-quality existing docstrings
* Improve and standardize documentation style
* Preserve developer-written docs when appropriate
* Provide documentation coverage insights
* Highlight undocumented functions

---

### 🔹 Multi-Language Code Support

Extend beyond Python to support additional programming languages:

* JavaScript / TypeScript
* Java / Kotlin
* Go / Rust


Key capabilities:

* Automatic language detection
* Language-specific parsing strategies
---

## ☁️ Deployment

The application is deployed on Streamlit Community Cloud for zero-cost public access.

Future deployment targets include:

* Docker containers
* AWS / Azure / GCP cloud environments

---