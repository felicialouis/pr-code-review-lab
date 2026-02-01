import json
import hashlib
from utils import is_empty

DATA_PATH = "data/users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    if is_empty(username):
        raise ValueError("Username cannot be empty")

    if is_empty(password) or len(password) < 6:
        raise ValueError("Password must be at least 6 characters")

    with open(DATA_PATH) as f:
        users = json.load(f)

    users.append({
        "username": username,
        "password": hash_password(password)
    })

    with open(DATA_PATH, "w") as f:
        json.dump(users, f, indent=2)
