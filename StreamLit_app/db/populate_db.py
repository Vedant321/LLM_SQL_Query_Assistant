from .postgres import PostgresDB
import os

db = PostgresDB()

sql_file = os.path.join(os.path.dirname(__file__), "../movies_db.sql")

if not os.path.exists(sql_file):
    print("SQL file not found!")
else:
    with open(sql_file, "r") as f:
        sql_script = f.read()

    result = db.execute_script(sql_script)
    print(result)
