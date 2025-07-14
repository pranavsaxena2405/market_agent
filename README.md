**Marketing AI Agent**

**Overview**
Welcome to the Marketing AI Agent! This project is an intelligent assistant that answers complex marketing queries (e.g., "Best ad copy for summer sale campaigns") using a Retrieval-Augmented Generation (RAG) pipeline. It leverages 20 marketing blog files, FAISS for vector search, and Groq's llama3-70b-8192 LLM, deployed on PythonAnywhere. Perfect for marketers or developers looking to experiment with AI-driven content retrieval!
Features

**Smart Retrieval**: 
Uses FAISS to find relevant ad copy and tips from blog data.
Natural Responses: Generates human-like answers with Groq's powerful LLM.
Public Access: Deployed on PythonAnywhere for easy testing.
Open-Source: Built with free, accessible tools.

**Installation**
To set up and run this project locally, follow these steps:
Prerequisites

Python 3.9+
Git (for cloning the repo)
pip (Python package manager)
A free Groq API key (sign up at groq.com)

**Steps**

**Clone the Repository**:
git clone https://github.com/yourusername/Marketing-AI-Agent.git
cd Marketing-AI-Agent


**Install Dependencies**:Create a virtual environment and install required packages:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


**Set Up Environment Variables**:Create a .env file in the root directory and add your Groq API key:
GROQ_API_KEY=your_groq_api_key_here

(Keep this file out of version control by adding .env to .gitignore.)

Generate Blog Data (Optional):If the blog files aren’t included, run the script to create them:
python create_blogs_zip.py

This generates summer_sale_blogs.zip with 20 .txt files.

**Run the Application**:Start the FastAPI server locally:
uvicorn agent.py:app --reload

Access it at http://127.0.0.1:8000/docs in your browser.


Usage

API Endpoint: Send a POST request to /run-agent with a JSON body like:
{
  "query": "Best ad copy for summer sale campaigns"
}

Example using curl:
curl -X POST "http://127.0.0.1:8000/run-agent" -H "Content-Type: application/json" -d '{"query":"Best ad copy for summer sale campaigns"}'


Expected Output: A JSON response with the answer and source documents.

Test Queries:

"Combine emotional appeal with urgency for e-commerce."
"Optimize ad copy for Instagram flash sales."
Try the five complex queries from our earlier discussion!



Deployment (PythonAnywhere): optional
To deploy on PythonAnywhere (free tier):

Sign up at pythonanywhere.com.
Upload the repo files via the “Files” tab.
Create a fastapi_wsgi.py file:from agent import app


Set up a Web app with WSGI configuration, pointing to fastapi_wsgi.py.
Add your Groq API key in the “Consoles” tab via environment variables.
Access the app at your PythonAnywhere URL (e.g., https://yourusername.pythonanywhere.com/docs).

**Technologies**

Languages/Frameworks: Python, FastAPI
Libraries: LangChain, sentence-transformers, FAISS, langchain-groq
Hosting: PythonAnywhere
LLM: Groq llama3-70b-8192


