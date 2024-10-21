from dotenv import load_dotenv
from langchain.chains import RetrievalQA

from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

from redundant_filter_retriever import RedundantFilterRetriever

#to debug
import langchain
# then set debug to True
langchain.debug = True

#load API key from .env file
load_dotenv()

#if I use ChatOpenAI, when I use map_reduce, I get an error.
# chat = ChatOpenAI(verbose=True)
chat = OpenAI()
embeddings = OpenAIEmbeddings()

#Create a Chroma object
db = Chroma(
    persist_directory="emb",
    embedding_function=embeddings
)

# Create a RedundantFilterRetriever object
redundant_filter_retriever = RedundantFilterRetriever(
    embeddings=embeddings, 
    chroma=db
)

# Create a RetrievalQA object using from_chain_type
chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="stuff",
    retriever=redundant_filter_retriever,
    verbose=True # This doesn't seem to work
)

# Prompt user for input
user_input = input("Please enter your query: ")
print(f"You entered: {user_input}")

# Use the RetrievalQA chain to process the query
result = chain.run(user_input)

# Print the result
print("result", result)