import json
import os
from user_service import register_user

DATA_PATH = "data/users.json"


def test_register_user_success(tmp_path, monkeypatch):
    test_file = tmp_path / "users.json"
    test_file.write_text("[]")

    monkeypatch.setattr("user_service.DATA_PATH", str(test_file))

    register_user("alice", "password123")

    data = json.loads(test_file.read_text())
    assert data[0]["username"] == "alice"
    assert data[0]["password"] != "password123"
