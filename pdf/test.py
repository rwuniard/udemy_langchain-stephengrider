from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler

from dotenv import load_dotenv

load_dotenv()

class StreamHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        print(f"Token: {token}")

print ("Hello test")

chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamHandler()]
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])

chain = LLMChain(llm=chat, prompt=prompt)

for output in chain.stream({"content": "Tell me a joke"}):
    print(output)

# messages = prompt.format_messages(content = "Tell me a joke")
# print(messages)

# for message in chat.stream(messages):
#     print(message)
# print(response)


