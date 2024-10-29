from typing import Any, Dict, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage

class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized: Dict[str, Any], messages: List[BaseMessage], **kwargs: Any) -> None:
        # print(f"Chat model started: {serialized}")
        print(f"Messages: {messages}")