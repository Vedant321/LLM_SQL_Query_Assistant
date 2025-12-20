import psycopg2
import pandas as pd
from config import DB_CONFIG

class PostgresDB:
    def __init__(self, config=DB_CONFIG):
        self.config = config

    def get_connection(self):
        """Return a new DB connection"""
        return psycopg2.connect(**self.config)

    def execute_query(self, query):
        """
        Execute SQL query and return a pandas DataFrame
        """
        try:
            conn = self.get_connection()
            df = pd.read_sql_query(query, conn)
            conn.close()
            return df
        except Exception as e:
            return f"Error: {e}"
    
    def execute_script(self, sql_script):
        """
        Execute multiple SQL statements (CREATE TABLE, INSERT, etc.)
        Handles multiple statements separated by semicolons.
        """
        try:
            conn = self.get_connection()
            cur = conn.cursor()
            statements = [s.strip() for s in sql_script.split(";") if s.strip()]

            for stmt in statements:
                cur.execute(stmt)

            conn.commit()
            cur.close()
            conn.close()
            return "Script executed successfully"
        except Exception as e:
            return f"Error: {e}"
