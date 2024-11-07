"""
Generate and store embeddings for the given pdf

1. Extract text from the specified PDF.
2. Divide the extracted text into manageable chunks.
3. Generate an embedding for each chunk.
4. Persist the generated embeddings.

:param pdf_id: The unique identifier for the PDF.
:param pdf_path: The file path to the PDF.

Example Usage:

create_embeddings_for_pdf('123456', '/path/to/pdf')
"""

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from typing import List, Dict
from app.chat.vector_stores.pinecone import vector_store

def create_embeddings_for_pdf(pdf_id: str, pdf_path: str) -> List[Dict]:
    """Generate and store embeddings for the given pdf"""
    
    # 1. Extract text from PDF
    loader = PyPDFLoader(pdf_path)

    
    # 2. Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    chunks = loader.load_and_split(text_splitter)
    
    print(f"Number of chunks: {len(chunks)}")
    for chunk in chunks:
        chunk.metadata = {
            "page": chunk.metadata.get("page", None),
            "text": chunk.page_content,
            "pdf_id": pdf_id
        }

    vector_store.add_documents(chunks)
