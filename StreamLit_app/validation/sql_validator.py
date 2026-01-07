import sqlparse


class SQLValidator:
    def __init__(self):
        # Restricted Operations
        self.forbidden_keywords = ["DROP", "DELETE", "TRUNCATE", "ALTER", "UPDATE", "INSERT"]

    def validate(self, sql):
        """
        Validate an LLM-generated SQL query before execution.
        Returns:
            (is_valid: bool, message: str)
        """
        warnings = []

        if not sql or not sql.strip():
            return False, "Empty SQL query"

        sql_upper = sql.upper()

        parsed = sqlparse.parse(sql)
        if not parsed:
            return False, "Unable to parse SQL"

        statement = parsed[0]

        if statement.get_type() != "SELECT":
            return False, "Only SELECT queries are allowed"

        # We don't want to execute such statements, hence blocking them
        for keyword in self.forbidden_keywords:
            if keyword in sql_upper:
                return False, f"Forbidden operation detected: {keyword}"
        
        if "SELECT *" in sql_upper:
            warnings.append(
                "Avoid using SELECT *. Specify required columns for better performance.")

        # We delibrately want to limit the number of rows as it can cause the app to crash.
        if "LIMIT" not in sql_upper:
            return False, "LIMIT clause is required"
        

        return True, "Query passed validation", warnings

# Test Case1:
# sql1 = SQLValidator()
# print(sql1.validate("Select * from movies where (DELETE from movies);"))

# Test Case2:
sql2 = SQLValidator()
print(sql2.validate("Select * from movies limit 10;"))