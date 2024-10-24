import sqlite3
from langchain.tools import Tool


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

# Create a tool for executing SQL queries
run_query_tool = Tool.from_function(
    name="execute_sql",
    description="Execute a SQL query and return the results",
    func=execute_sql
)