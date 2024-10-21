from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever, Document
from typing import List
import asyncio

# This Class RedundantFilterRetriever is used to remove redundant embeddings inside Chroma DB
class RedundantFilterRetriever(BaseRetriever):
    embeddings : Embeddings
    chroma : Chroma 

    def get_relevant_documents(self, query: str) -> List[Document]:
        
        # Calculate the embedding of the query
        query_embedding = self.embeddings.embed_query(query)
        # Take the query_embedding and feed it to the max_marginal_search_by_vector
        return asyncio.run (self.chroma.asimilarity_search_by_vector(query_embedding, k=4))
    
    async def aget_relevant_documents(self) -> List[Document]:
        return []   
    