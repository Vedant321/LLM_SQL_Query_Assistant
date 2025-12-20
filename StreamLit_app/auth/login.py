import streamlit as st
from auth.users import validate_user

def login_page():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.markdown("<h1>🎬 Intelligent Movie Query Assistant</h1>", unsafe_allow_html=True)

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    username = st.text_input("Email or Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign In"):
        if validate_user(username, password):
            st.session_state.logged_in = True
            st.success("Signed in successfully!")
        else:
            st.error("Incorrect username or password")

    st.markdown("</div>", unsafe_allow_html=True)

    return st.session_state.logged_in
