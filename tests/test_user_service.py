import json
import os
from user_service import register_user

DATA_PATH = "data/users.json"


def test_register_user_success(tmp_path):
    test_file = tmp_path / "users.json"
    test_file.write_text("[]")

    register_user("alice", "password123", data_path=str(test_file))

    data = json.loads(test_file.read_text())
    assert data[0]["username"] == "alice"
    assert data[0]["password"] != "password123"
