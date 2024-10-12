from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder

from langchain.memory import ConversationBufferMemory

from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

# In order to understand the code, you need to have a basic understanding of the following concepts from 
# section 3 of the course. (look at the tchat.pdf diagram)

def main():
    chat = ChatOpenAI()

    memory = ConversationBufferMemory(
        memory_key="messages",
        return_messages=True
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
        memory=memory
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