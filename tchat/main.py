from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder

# from langchain.memory import ConversationBufferMemory, FileChatMessageHistory
# using the ConversationSummaryMemory instead of the ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# In order to understand the code, you need to have a basic understanding of the following concepts from 
# section 3 of the course. (look at the tchat.pdf diagram)

def main():
    chat = ChatOpenAI(verbose=True) 

    # memory = ConversationBufferMemory(
    #     memory_key="messages",
    #     return_messages=True,
    #     chat_memory=FileChatMessageHistory("messages.json")
    # )
    # using the ConversationSummaryMemory instead of the ConversationBufferMemory
    memory = ConversationSummaryMemory(
        memory_key="messages",
        return_messages=True,
        llm=chat # this is the chat model that will be used to summarize the conversation
        # chat_memory=FileChatMessageHistory("messages.json")
    )

    prompt = ChatPromptTemplate(
        input_variables = ["content", "messages"],
        messages = [
            MessagesPlaceholder(variable_name="messages"),
            HumanMessagePromptTemplate.from_template("{content}"),
        ]
    )

    chain = LLMChain(
        llm = chat,
        prompt = prompt,
        output_key = "response",
        memory=memory,
        verbose=True # This will print the prompt and response to the console
    )


    while True:
        user_input = input(">>> ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = chain({
            "content": user_input
        })
        print(result["response"])

if __name__ == "__main__":
    main()