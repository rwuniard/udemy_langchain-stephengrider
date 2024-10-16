from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter


load_dotenv()

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=100
)

loader = TextLoader("facts.txt")
document = loader.load_and_split(
    text_splitter=splitter
)

for item in document:
    print(item.page_content, "\n")