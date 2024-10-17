from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma


load_dotenv()

embeddings = OpenAIEmbeddings()

emb = embeddings.embed_query("Hello, how are you?")
print(emb)

# splitter = CharacterTextSplitter(
#     separator="\n",
#     chunk_size=200,
#     chunk_overlap=0
# )

# loader = TextLoader("facts.txt")
# document = loader.load_and_split(
#     text_splitter=splitter
# )

# for item in document:
#     print(item.page_content, "\n")