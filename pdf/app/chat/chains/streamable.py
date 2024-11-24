from queue import Queue
from threading import Thread
from app.chat.callbacks.stream import StreamHandler

from flask import current_app


class StreamableChain:
    def stream(self, input, config=None, **kwargs):
        queue = Queue()
        stream_handler = StreamHandler(queue)

        def task(app_context):
            app_context.push()
            self(input, callbacks=[stream_handler])

        # Start the task in a separate thread. 
        # This will allow the main thread to yield tokens to the caller.
        Thread(target=task, args=[current_app.app_context()]).start()

        while True:
            token = queue.get()
            if token is None:
                break
            yield token