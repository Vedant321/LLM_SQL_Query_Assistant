from config import AUTH_USERS


def validate_user(username, password):
    """
    Check if username/password pair exists.
    AUTH_USERS is a dictionary from config.py
    """
    if not AUTH_USERS:
        return False  # no users configured
    return username in AUTH_USERS and AUTH_USERS[username] == password
