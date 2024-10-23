import sqlite3
from langchain.tools import Tool


conn = sqlite3.connect("db.sqlite")

def execute_sql(query: str) -> str:
    cursor = conn.cursor()
    try:    
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.OperationalError as err:
        return f"An error occurred: {str(err)}"

run_query_tool = Tool.from_function(
    name="execute_sql",
    description="Execute a SQL query and return the results",
    func=execute_sql
)