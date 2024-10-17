from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.chroma import Chroma


load_dotenv()

embeddings = OpenAIEmbeddings()

# emb = embeddings.embed_query("Hello, how are you?")
# print(emb)

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

loader = TextLoader("facts.txt")
document = loader.load_and_split(
    text_splitter=splitter
)

db = Chroma.from_documents(
    document,
    embedding=embeddings,
    persist_directory="emb"
)

# The results is a tuple containing the document and the score
results = db.similarity_search_with_score("What is an interesting fact about English language?")

for result in results:
    print("\n")
    print(result[1]) # print the score
    print(result[0].page_content) # print the content

# for item in document:
#     print(item.page_content, "\n")