import sqlite3

conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()



# Find all the tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
for table in tables:
    print(f"Table Name: {table[0]}")
    cursor.execute(f"PRAGMA table_info({table[0]})")
    schema = cursor.fetchall()
    for column in schema:
        print(f"Column Name: {column[1]}, Column Type: {column[2]}")    



