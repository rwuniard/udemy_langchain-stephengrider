from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate

def main():
    prompt = ChatPromptTemplate(
        input_variables = ["content"],
        messages = [
            HumanMessagePromptTemplate.from_template("{content}"),
        ]
    )
    user_input = input(">>> ")
    print(f"You entered: {user_input}")

if __name__ == "__main__":
    main()