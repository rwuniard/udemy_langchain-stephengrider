from dotenv import load_dotenv
from langchain.chains import RetrievalQA

from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

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

# Create a RetrievalQA object using from_chain_type
chain = RetrievalQA.from_chain_type(
    llm=chat,
    chain_type="map_reduce",
    retriever=db.as_retriever(),
    verbose=True
)

# Prompt user for input
user_input = input("Please enter your query: ")
print(f"You entered: {user_input}")

# Use the RetrievalQA chain to process the query
result = chain.run(user_input)

# Print the result
print("result", result)