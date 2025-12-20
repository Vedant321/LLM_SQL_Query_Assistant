from openai import OpenAI
from config import OPENAI_API_KEY


class SQLGenerator:
    def __init__(self, api_key=OPENAI_API_KEY):
        self.client = OpenAI(api_key=api_key)

    def generate(self, user_query: str) -> str:
        """
        Generate SQL query from a natural language query.
        Returns only SQL code as a string.
        """
        table_schema = """-- MOVIES TABLE
        movies(
            movie_id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            release_year INT,
            duration_minutes INT,
            rating FLOAT,
            revenue_million FLOAT
        )

        genres(
            genre_id SERIAL PRIMARY KEY,
            genre_name TEXT UNIQUE
        )

        movie_genres(
            movie_id INT REFERENCES movies(movie_id),
            genre_id INT REFERENCES genres(genre_id),
            PRIMARY KEY(movie_id, genre_id)
        )

        actors(
            actor_id SERIAL PRIMARY KEY,
            actor_name TEXT
        )

        movie_cast(
            movie_id INT REFERENCES movies(movie_id),
            actor_id INT REFERENCES actors(actor_id),
            PRIMARY KEY(movie_id, actor_id)
        )

        directors(
            director_id SERIAL PRIMARY KEY,
            director_name TEXT
        )

        movie_directors(
            movie_id INT REFERENCES movies(movie_id),
            director_id INT REFERENCES directors(director_id),
            PRIMARY KEY(movie_id, director_id)
        )

        
        ratings(
            rating_id SERIAL PRIMARY KEY,
            movie_id INT REFERENCES movies(movie_id),
            user_id INT,
            rating FLOAT,
            rating_date DATE
        )"""

        prompt = f""" You are a SQL assistant. The database has the following table schema:

                {table_schema}

                Generate a SQL query to answer this user request:
                "{user_query}"

                Return ONLY the SQL query, no explanations. Do NOT add explanations, extra words, or code fences. Drop duplicate columns.
                """

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a SQL assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150
            )

            sql_query = response.choices[0].message.content.strip()

            prefixes = ["sql", "SQL:", "```sql", "```"]

            for prefix in prefixes:
                if sql_query.startswith(prefix):
                    sql_query = sql_query[len(prefix):].strip()

            return sql_query

        except Exception as e:
            return f"Error generating SQL: {e}"
