from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)

from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from tools.sql import run_query_tool, list_tables

from dotenv import load_dotenv

load_dotenv()   

chat = ChatOpenAI()

tables = list_tables()
# print(tables)

# Create a prompt template for the agent
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=f"You are an AI that has access to SQLite database, \n{tables}"
        ),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Create a list of tools for the agent
tools = [run_query_tool]

# Create an agent with the prompt and tools
agent = OpenAIFunctionsAgent(
    llm=chat, 
    prompt=prompt,
    tools = tools
)

# Create an agent executor with the agent and tools
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# agent_executor("What are the tables in the database and their columns? Ensure that you use SQLLite syntax.")
# agent_executor("How many users are there in the database?")
# agent_executor(
#     "how many users provided shipping address in the database? The user address is stored in the table called addresses.")
agent_executor("How many users provided a shipping address?")