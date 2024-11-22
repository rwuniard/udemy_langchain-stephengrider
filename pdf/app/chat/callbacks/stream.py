from langchain_core.callbacks.base import BaseCallbackHandler
from queue import Queue

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