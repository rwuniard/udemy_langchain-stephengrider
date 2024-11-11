import os

import pinecone
# from langchain.vectorstores import Pinecone
from langchain.vectorstores.pinecone import Pinecone

from app.chat.embeddings.openai import embeddings
from app.chat.models import ChatArgs

pinecone.Pinecone(
    api_key=os.getenv("PINECONE_API_KEY"),
    environment=os.getenv("PINECONE_ENV_NAME")
)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"), 
    embeddings
)

def build_retriever(chat_args: ChatArgs):
    return vector_store.as_retriever(
        search_kwargs={
            "filter": {"pdf_id": chat_args.pdf_id}
        }
    )
