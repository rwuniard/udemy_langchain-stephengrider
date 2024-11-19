from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler

from dotenv import load_dotenv

load_dotenv()

class StreamHandler(BaseCallbackHandler):
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # print(f"Token: {token}")
        pass

print ("Hello test")

chat = ChatOpenAI(
    streaming=True,
    callbacks=[StreamHandler()]
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])
class StreamingChain(LLMChain):
    def stream(self, input, config=None, **kwargs):
        print(self(input))
        yield 'hi'
        yield 'there'

chain = StreamingChain(llm=chat, prompt=prompt)

for output in chain.stream(input = {"content": "Tell me a joke"}):
    print(output)


# chain = LLMChain(llm=chat, prompt=prompt)

# for output in chain.stream({"content": "Tell me a joke"}):
#     print(output)

# messages = prompt.format_messages(content = "Tell me a joke")
# print(messages)

# for message in chat.stream(messages):
#     print(message)
# print(response)


