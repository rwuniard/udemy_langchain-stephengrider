from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()


def main():
    chat = ChatOpenAI()
    # chat.load_api_key()

    prompt = ChatPromptTemplate(
        input_variables = ["content"],
        messages = [
            HumanMessagePromptTemplate.from_template("{content}"),
        ]
    )

    chain = LLMChain(
        llm = chat,
        prompt = prompt,
        output_key = "response"
    )


    user_input = input(">>> ")
    result = chain({
        "content": user_input
    })
    # print(f"You entered: {user_input}")
    print(result["response"])

if __name__ == "__main__":
    main()