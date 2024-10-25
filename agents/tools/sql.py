import sqlite3
from langchain.tools import Tool
from pydantic.v1 import BaseModel #langchain uses pydantic v1
from typing import List
conn = sqlite3.connect("db.sqlite")

# List all tables in the database
def list_tables():
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    rows = cursor.fetchall()
    return "\n".join(row[0] for row in rows if row[0] is not None)

# Execute a SQL query and return the results
def execute_sql(query: str) -> str:
    cursor = conn.cursor()
    try:    
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as err:
        return f"An error occurred: {str(err)}"
    
# This is the input schema for the run_query_tool
class RunQueryArgsSchema(BaseModel):
    query: str

# Create a tool for executing SQL queries
run_query_tool = Tool.from_function(
    name="execute_sql",
    description="Execute a SQL query and return the results",
    func=execute_sql,
    args_schema=RunQueryArgsSchema
)

# Describe all tables in the database
def describe_tables(table_names):
    print("executing describe_tables")
    cursor = conn.cursor()
    # tables = ", ".join(f"'{table}'" for table in table_names)
    # print(tables)

  # Convert input to a list if it's a string
    if isinstance(table_names, str):
        table_names = [name.strip() for name in table_names.split()]
    
    # Create a properly formatted string of table names
    tables = ", ".join(f"'{table.strip()}'" for table in table_names)
    
    print(f"Tables to describe: {tables}") # Debugging line
    

    rows = cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name IN ({tables});")
    print("rows fetched")
    print("\n".join(row[0] for row in rows if row[0] is not None))
    return "\n".join(row[0] for row in rows if row[0] is not None)

class DescribeTableArgsSchema(BaseModel):
    table_names: List[str]

describe_table_tool = Tool.from_function(
    name="describe_tables",
    description="Given a list of table names, return the SQL schema for each table",
    func=describe_tables,
    args_schema=DescribeTableArgsSchema
)