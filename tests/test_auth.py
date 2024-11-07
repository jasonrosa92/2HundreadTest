import pytest
from app.auth.jwt import create_access_token, verify_access_token

def test_create_access_token():
    data = {"sub": "test_user"}
    token = create_access_token(data)
    assert token is not None
    assert isinstance(token, str)

def test_verify_access_token():
    data = {"sub": "test_user"}
    token = create_access_token(data)
    verified_data = verify_access_token(token)
    assert verified_data.get("sub") == "test_user"
