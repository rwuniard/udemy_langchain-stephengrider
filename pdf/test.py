from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks.base import BaseCallbackHandler

from dotenv import load_dotenv
from queue import Queue
from threading import Thread

load_dotenv()


class StreamHandler(BaseCallbackHandler):
    def __init__(self, queue: Queue):
        self.queue = queue

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # Put the token into the queue.
        self.queue.put(token)

    def on_llm_end(self, response, **kwargs) -> None:
        self.queue.put(None)

    def on_llm_error(self, error: Exception, **kwargs) -> None:
        self.queue.put(None)

print ("Hello test")

chat = ChatOpenAI(
    streaming=True
)

prompt = ChatPromptTemplate.from_messages([
    ("human", "{content}")
])
class StreamingChain(LLMChain):
    def stream(self, input, config=None, **kwargs):
        queue = Queue()
        stream_handler = StreamHandler(queue)

        def task():
            self(input, callbacks=[stream_handler])

        # Start the task in a separate thread. 
        # This will allow the main thread to yield tokens to the caller.
        Thread(target=task).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token

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


