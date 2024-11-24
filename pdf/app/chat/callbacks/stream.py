from langchain_core.callbacks.base import BaseCallbackHandler
from queue import Queue

class StreamHandler(BaseCallbackHandler):
    def __init__(self, queue: Queue):
        self.queue = queue
        self.streaming_run_ids = set()

    def on_chat_model_start(self, serialized, messages, run_id, **kwargs) -> None:
        if serialized['kwargs']['streaming']:
            # print("This is streaming model, I should listen to streaming evennts with run_id" , run_id)
            self.streaming_run_ids.add(run_id)
    def on_llm_new_token(self, token: str, **kwargs) -> None:
        # Put the token into the queue.
        self.queue.put(token)

    def on_llm_end(self, response, **kwargs) -> None:
        if kwargs['run_id'] in self.streaming_run_ids:
            self.queue.put(None)
            self.streaming_run_ids.remove(kwargs['run_id'])

    def on_llm_error(self, error: Exception, **kwargs) -> None:
        if kwargs['run_id'] in self.streaming_run_ids:
            self.queue.put(None)
            self.streaming_run_ids.remove(kwargs['run_id'])