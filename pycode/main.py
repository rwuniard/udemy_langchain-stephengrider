import argparse
import os

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


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
# openAIKey = os.getenv('OPENAI_API_KEY')
# if not openAIKey:
#     raise ValueError("The OPENAI_API_KEY environment variable is not set.")

# llm = OpenAI(api_key = openAIKey)

# This will load the OpenAI API key from the environment variable.
llm = OpenAI()

# Create a prompt template.
code_template = PromptTemplate(
    template = "Write a very short {language} function that will {task}",
    input_variables=["language", "task"]
)

unittest_template = PromptTemplate(
    template = "Write a unittest for the following {language} code:\n {code}",
    input_variables=["language", "code"]
)

# Create a code chain
code_chain = LLMChain(
    llm = llm,
    prompt = code_template,
    output_key="code"
)

# Create a unittest chain
unittest_chain = LLMChain(
    llm = llm,
    prompt = unittest_template,
    output_key="unit_test_code"
)

chain = SequentialChain(
    chains = [code_chain, unittest_chain],
    input_variables=["language", "task"],
    output_variables=["code", "unit_test_code"]
)

# Chain the input into the code chain and get the result.
result = chain({
    "language": language,
    "task": task
})

print(result["code"])
print(result["unit_test_code"])
# Print the result with the text key format.
# print(result["text"])

# when you specify the output_key as code, you need to use "code" key to get the result.
# print(result["code"]) 


# Simple example to use the llm
# poem = llm("Write a very short poem")
# print(poem)