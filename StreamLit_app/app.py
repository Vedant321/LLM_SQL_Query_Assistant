from auth.login import login_page
from query_page import main_page
import pathlib


def load_css():
    css_path = pathlib.Path(__file__).parent / "styles/netflix.css"
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


# Show login page first
if login_page():
    main_page()

#streamlit run app.py --server.runOnSave true
# Sample queries:
#1. Give me list of all action movies.
#2. Give me list of all actors and their movies who's name starts with T