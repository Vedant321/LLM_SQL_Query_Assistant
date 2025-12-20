import streamlit as st
import pandas as pd
from db.postgres import PostgresDB
from gpt.sql_generator import SQLGenerator

def main_page():
    st.markdown("<h1>🍿 Movie Database Explorer</h1>", unsafe_allow_html=True)

    st.sidebar.title("🧭 Need Ideas?")

    st.sidebar.markdown("### 🎯 Try asking things like:")

    st.sidebar.write("• *Show me the most popular movies*")
    st.sidebar.write("• *Which movies came out in 2020?*")
    st.sidebar.write("• *List action movies*")
    st.sidebar.write("• *Who acted in Inception?*")
    st.sidebar.write("• *What are the top-rated comedies?*")

    st.sidebar.markdown("### 🔍 Tips")
    st.sidebar.info(
        "You can type your question in simple English. "
        "**Example:** \"Find movies with Brad Pitt\""
    )

    st.sidebar.markdown("### ⭐ Fun suggestions")
    st.sidebar.write("• *Show movies similar to Interstellar*")
    st.sidebar.write("• *Give me some family-friendly films*")
    st.sidebar.write("• *What are good horror movies to watch tonight?*")


    db = PostgresDB()
    sql_gen = SQLGenerator()

    # User Query Section
    st.markdown("<div class='netflix-card'>", unsafe_allow_html=True)
    user_input = st.text_input("Ask something about movies…")
    st.markdown("</div>", unsafe_allow_html=True)

    # Generate SQL
    if st.button("Generate SQL"):
        if user_input:
            sql_query = sql_gen.generate(user_input)
            st.markdown("<div class='netflix-card'>", unsafe_allow_html=True)
            st.subheader("🧠 Generated SQL")
            st.code(sql_query, language='sql')
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a query.")

    # Execute SQL
    if st.button("Run Query"):
        if user_input:
            sql_query = sql_gen.generate(user_input)
            result = db.execute_query(sql_query)
            st.markdown("<div class='netflix-card'>", unsafe_allow_html=True)
            st.subheader("📊 Results")
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
            else:
                st.error(result)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("Please enter a query.")
