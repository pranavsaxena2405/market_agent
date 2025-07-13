from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def run_query(query: str) -> str:
    # Use open-source HuggingFace embedding model (no OpenAI dependency)
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    # Load the FAISS vector index built using blog chunks
    vectorstore = FAISS.load_local("faiss_index", embedding_model, allow_dangerous_deserialization=True)

    retriever = vectorstore.as_retriever()

    # Initialize Groq's LLaMA3-70B model for answer generation
    llm = ChatGroq(
        model_name="llama3-70b-8192",
        api_key=os.getenv("GROQ_API_KEY"),
        temperature=0.7
    )

    # Create RAG pipeline using LangChain's RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )

    # Run query and return response
    return qa_chain.run(query)
