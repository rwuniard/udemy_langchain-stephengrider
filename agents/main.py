from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    HumanMessagePromptTemplate,
)

from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from tools.sql import run_query_tool, list_tables, describe_tables, describe_table_tool
from tools.report import write_report_tool
from langchain.memory import ConversationBufferMemory
from handlers.chat_model_start_handler import ChatModelStartHandler

from dotenv import load_dotenv

load_dotenv()   

# Create a handler for the chat model
handler = ChatModelStartHandler()

# Create a chat model
chat = ChatOpenAI(
    callbacks=[handler]
    )

tables = list_tables()
# print(tables)

# table_description = describe_tables(tables)
# print(table_description)

# Create a prompt template for the agent
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=(
                "You are an AI that has access to SQLite database \n"
                 f"The database has tables of: {tables}\n"
                 "You can use the describe_tables_tool to get the schema of a table.\n"
                 "Do not make any assumptions about what tables exists "
                 "or what columns they have."
            )
        ),
        MessagesPlaceholder(variable_name="chat_history"), # this is to store the conversation history
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)

# Create a memory buffer to store the conversation history
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True # this is to return messages objects instead of strings
)

# Create a list of tools for the agent
tools = [
    run_query_tool,
    describe_table_tool,
    write_report_tool
]

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
    # verbose=True,
    memory=memory
)

# agent_executor("What are the tables in the database and their columns? Ensure that you use SQLLite syntax.")
# agent_executor("How many users are there in the database?")
# agent_executor(
#     "how many users provided shipping address in the database? The user address is stored in the table called addresses.")
# agent_executor("How many users provided shipping address?")
# agent_executor("Show me the first 10 user address in the database")
# agent_executor("Show me the top 5 address with FL state")
# agent_executor("What is the average order value?")
# agent_executor("Summarize the top 5 popular products. Write a report and save it as report.html")
agent_executor("How many orders are there in the database? Write a report and save it as report.html")
agent_executor("Repeat the same process for users")