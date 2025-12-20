import os
import streamlit as st

# Load secrets from Streamlit first, fallback to environment
def get_secret(key, default=None):
    if hasattr(st, "secrets") and key in st.secrets:
        return st.secrets[key]
    return os.environ.get(key, default)

# ---------------- AUTH CONFIG ----------------
# Stored as dictionary {username: password}
raw_users = get_secret("AUTH_USERS", "")
AUTH_USERS = dict(
    pair.split(":") for pair in raw_users.split(",") if ":" in pair
)

# ---------------- DATABASE CONFIG ----------------
DB_CONFIG = {
    "host": get_secret("DB_HOST"),
    "database": get_secret("DB_NAME"),
    "user": get_secret("DB_USER"),
    "password": get_secret("DB_PASSWORD"),
    "port": int(get_secret("DB_PORT", 5432)),
}

# ---------------- OPENAI API KEY ----------------
OPENAI_API_KEY = get_secret("OPENAI_API_KEY")
