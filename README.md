# Project-CRV2

**Project-CRV2** is a chatbot-powered query system for analyzing a dataset of business contacts. It leverages OpenAI embeddings, Pinecone for vector similarity search, and a streamlined Python workflow for efficient data querying.

---

## **Features**
- **Query Contact Database**: Run advanced queries such as "How many senior decision-makers are in manufacturing companies in Hampshire?"
- **OpenAI Integration**: Uses `text-embedding-ada-002` for generating embeddings.
- **Vector Search**: Powered by Pinecone to retrieve relevant results based on embeddings.
- **Streamlined Codebase**: Well-organized Python scripts for generating embeddings, uploading them to Pinecone, and querying results.
- **GitHub Integration**: Easily manage and share project code.

---

## **Setup**

### **Requirements**
- Python 3.12+
- Virtual Environment (`venv`)
- Installed libraries:
  - `openai`
  - `pinecone-client`
  - `pandas`

---

### **Installation**

#### **Step 1: Clone the repository**
```bash
git clone https://github.com/your-username/Project-CRV2.git
cd Project-CRV2
#### **Step 2: Set up the virtual environment**

For Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
