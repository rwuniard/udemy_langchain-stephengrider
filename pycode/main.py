import argparse
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


# Create the argument parser.
parser = argparse.ArgumentParser(description="Process some tasks.")
parser.add_argument('--task', type=str, required=True, help='The task to be processed')
parser.add_argument('--language', type=str, required=True, help='The language to be used')

# Parse the arguments
args = parser.parse_args()

# Use the task and language arguments.
task = args.task
language = args.language

# Load the environment variables
load_dotenv()
# Load the OpenAI API key from the environment variable.
openAIKey = os.getenv('OPENAI_API_KEY')
if not openAIKey:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")

llm = OpenAI(api_key = openAIKey)

# Create a prompt template.
promptTemplate = PromptTemplate(
    template = "Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
    )

# Create a code chain
code_chain = LLMChain(
    llm = llm,
    prompt = promptTemplate
)

# Chain the input into the code chain and get the result.
result = code_chain({
    "language": "Python",
    "task": "list of numbers"
})

# Print the result with the text key format.
print(result["text"])


# Simple example to use the llm
# poem = llm("Write a very short poem")
# print(poem)