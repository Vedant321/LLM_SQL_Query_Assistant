import streamlit as st
import pandas as pd
from db.postgres import PostgresDB
from gpt.sql_generator import SQLGenerator
from validation.sql_validator import SQLValidator


def main_page():
    st.markdown("<h1>🍿 Movie Database Explorer</h1>", unsafe_allow_html=True)

    st.sidebar.title("🧭 Need Ideas?")
    st.sidebar.markdown("### 🎯 Try asking things like:")
    st.sidebar.write("• Show me the most popular movies")
    st.sidebar.write("• Which movies came out in 2020?")
    st.sidebar.write("• List action movies")
    st.sidebar.write("• Who acted in Inception?")
    st.sidebar.write("• What are the top-rated comedies?")

    db = PostgresDB()
    sql_gen = SQLGenerator()
    validator = SQLValidator()

    user_input = st.text_input("Ask something about movies…")

    if st.button("Generate SQL"):
        if user_input:
            sql_query = sql_gen.generate(user_input)
            st.session_state.generated_sql = sql_query

            st.subheader("🧠 Generated SQL")
            st.code(sql_query, language="sql")
        else:
            st.warning("Please enter a query.")

    # Run Query
    if st.button("Run Query"):
        sql_query = st.session_state.get("generated_sql")

        if not sql_query:
            st.warning("Please generate SQL before running the query.")
            return

        is_valid, message, warnings = validator.validate(sql_query)

        st.subheader("🛡️ Validation Result")

        if not is_valid:
            st.error(message)
        else:
            st.success(message)

        for warning in warnings:
            st.warning(warning)

        if is_valid:
            result = db.execute_query(sql_query)

            st.subheader("📊 Results")
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
            else:
                st.error(result)