from typing import Any, Dict, List
from langchain.callbacks.base import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from pyboxen import boxen


def boxen_print(*args, **kwargs):
    print(boxen(*args, **kwargs))

boxen_print("TEXT here", color="red", title= "Human Message")

class ChatModelStartHandler(BaseCallbackHandler):
    def on_chat_model_start(self, serialized: Dict[str, Any], messages: List[BaseMessage], **kwargs: Any) -> None:
        print("\n\n\n\n===== Sending messages to the model =====")
        for message in messages[0]:
            print(message.type)
            if message.type == "system":
                boxen_print(message.content, color="blue", title="System Message")
            elif message.type == "human":
                boxen_print(message.content, color="green", title="Human Message")
            elif message.type == "ai" and "function_call" in message.additional_kwargs:
                boxen_print(message.content, color="yellow", title="AI Message with Function Call")
            elif message.type == "ai":
                boxen_print(message.content, color="yellow", title="AI Message")
            elif message.type == "function":
                boxen_print(message.content, color="magenta", title="Function Message")
            else:
                boxen_print(message.content, color="white", title="Unknown Message")