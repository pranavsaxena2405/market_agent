from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

def build_faiss_index():
    folder_path = "data/blogs"  # Ensure it's relative for cross-platform support
    
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"❌ Folder {folder_path} not found.")
    
    docs = []

    # Load each .txt file using UTF-8 encoding
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            loader = TextLoader(file_path, encoding="utf-8")
            docs.extend(loader.load())

    if not docs:
        raise ValueError("❌ No text documents found in the folder!")

    # Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    split_docs = text_splitter.split_documents(docs)

    # Use HuggingFace sentence transformer for embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Build and save FAISS vector index
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    vectorstore.save_local("faiss_index")

    print("✅ FAISS index successfully created using HuggingFace embeddings.")
