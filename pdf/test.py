from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from dotenv import load_dotenv

load_dotenv()

print ("Hello test")

chat = ChatOpenAI(streaming=True)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

messages = prompt.format_messages(content = "Tell me a joke")
# print(messages)

for message in chat.stream(messages):
    print(message)
# print(response)


