import json
import hashlib

DATA_PATH = "data/users.json"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def login(username, password, data_path=DATA_PATH):
    with open(data_path) as f:
        users = json.load(f)

    hashed_input = hash_password(password)

    for u in users:
        if u["username"] == username and u["password"] == hashed_input:
            return "LOGIN SUCCESS"

    return "LOGIN FAILED"