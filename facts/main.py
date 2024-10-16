from dotenv import load_dotenv
from langchain.document_loaders import TextLoader


load_dotenv()

loader = TextLoader("facts.txt")
document = loader.load()

print(document)