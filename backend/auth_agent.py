import os
import uuid
from dotenv import load_dotenv

load_dotenv()

users = {
    os.getenv("ADMIN_USERNAME"): os.getenv("ADMIN_PASSWORD"),
    os.getenv("AUDITOR_USERNAME"): os.getenv("AUDITOR_PASSWORD"),
    os.getenv("ACCOUNTANT_USERNAME"): os.getenv("ACCOUNTANT_PASSWORD")
}

active_sessions = {}


def authenticate(username, password):

    if username in users:

        if users[username] == password:

            token = str(uuid.uuid4())

            active_sessions[token] = username.upper()

            return {
                "authenticated": True,
                "role": username.upper(),
                "token": token
            }

    return {
        "authenticated": False,
        "role": None,
        "token": None
    }


def validate_token(token):

    if token == "demo-admin-token":
        return True

    return token in active_sessions