from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamHandler

class StreamableChain:
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