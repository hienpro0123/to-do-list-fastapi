from fastapi.testclient import TestClient
from fastapi import FastAPI
from todo_app.db import setting
from sqlmodel import SQLModel, create_engine, Session
from todo_app.main import app, get_session
import pytest



connection_string = str(setting.TEST_DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string,
    echo=True
)

#========================================================================================
# Refactor with pytest fixture
# 1- Arrange, 2-Act, 3-Assert 4- Cleanup

@pytest.fixture(scope="module", autouse=True)
def get_db_session():
    SQLModel.metadata.create_all(engine)
    yield Session(engine)

@pytest.fixture(scope='function')
def test_app(get_db_session):
    def test_session():
        yield get_db_session
    app.dependency_overrides[get_session] = test_session
    with TestClient(app=app) as client:
        yield client

#=========================================================================================


# Test-1: root test
def test_root():
    client = TestClient(app=app)
    response = client.get('/')
    data = response.json()
    assert response.status_code == 200
    assert data == {"message": "Welcome to dailyDo todo app"}

# helper to register and login once
_token = None

def get_auth_header(client):
    global _token
    if _token is None:
        # create a test user
        payload = {"username":"testuser","email":"test@example.com","password":"pass"}
        client.post('/auth/register', json=payload)
        res = client.post('/auth/login', json={"username":"testuser","password":"pass"})
        _token = res.json()['access_token']
    return {"Authorization": f"Bearer {_token}"}

# Test-2 post test
def test_create_todo(test_app):
    test_todo = {"content":"create todo test", "is_completed":False}
    response = test_app.post('/todos/',json=test_todo, headers=get_auth_header(test_app))
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == test_todo["content"]

# Test-3 : get_all
def test_get_all(test_app):
    # SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     def db_session_ovrride():
    #         return session
    # app.dependency_overrides[get_session] = db_session_ovrride
    # client = TestClient(app=app)
    test_todo = {"content":"get all todos test", "is_completed":False}
    response = test_app.post('/todos/',json=test_todo)
    data = response.json()

    response = test_app.get('/todos/', headers=get_auth_header(test_app))
    new_todo = response.json()[-1]
    assert response.status_code == 200
    assert new_todo["content"] == test_todo["content"]

# Test-4 Sinlge todo
def test_get_single_todo(test_app):
    # SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     def db_session_ovrride():
    #         return session
    # app.dependency_overrides[get_session] = db_session_ovrride
    # client = TestClient(app=app)

    test_todo = {"content":"get single todo test", "is_completed":False}
    response = test_app.post('/todos/',json=test_todo)
    todo_id = response.json()["id"]

    res = test_app.get(f'/todos/{todo_id}', headers=get_auth_header(test_app))
    data = res.json()
    assert res.status_code == 200
    assert data["content"] == test_todo["content"]

# Test-5 : Edit Todo
def test_edit_todo(test_app):
    # SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     def db_session_ovrride():
    #         return session
    # app.dependency_overrides[get_session] = db_session_ovrride
    # client = TestClient(app=app)

    test_todo = {"content":"edit todo test", "is_completed":False}
    response = test_app.post('/todos/',json=test_todo)
    todo_id = response.json()["id"]

    edited_todo = {"content":"We have edited this", "is_completed":False}
    response = test_app.put(f'/todos/{todo_id}',json=edited_todo, headers=get_auth_header(test_app))
    data = response.json()
    assert response.status_code == 200
    assert data["content"] == edited_todo["content"]


# Test-6 Delete todo
def test_delete_todo(test_app):
    # SQLModel.metadata.create_all(engine)
    # with Session(engine) as session:
    #     def db_session_ovrride():
    #         return session
    # app.dependency_overrides[get_session] = db_session_ovrride
    # client = TestClient(app=app)

    test_todo = {"content":"delete todo test", "is_completed":False}
    response = test_app.post('/todos/',json=test_todo)
    todo_id = response.json()["id"]

    response = test_app.delete(f'/todos/{todo_id}', headers=get_auth_header(test_app))
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "Task successfully deleted"


# ------------------ user tests ------------------

def test_create_user(test_app):
    user_payload = {"username": "alice", "email": "alice@example.com", "password": "secret"}
    response = test_app.post('/users/', json=user_payload)
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == user_payload["username"]
    # password should not be returned
    assert "password" not in data and "hashed_password" not in data


def test_get_all_users(test_app):
    user_payload = {"username": "bob", "email": "bob@example.com", "password": "pass123"}
    _ = test_app.post('/users/', json=user_payload)

    response = test_app.get('/users/')
    data = response.json()
    assert response.status_code == 200
    assert any(u["username"] == user_payload["username"] for u in data)
    assert all("hashed_password" not in u for u in data)


def test_get_single_user(test_app):
    user_payload = {"username": "charlie", "email": "charlie@example.com", "password": "pwd"}
    resp = test_app.post('/users/', json=user_payload)
    user_id = resp.json()["id"]

    response = test_app.get(f'/users/{user_id}')
    data = response.json()
    assert response.status_code == 200
    assert data["email"] == user_payload["email"]
    assert "hashed_password" not in data


def test_delete_user(test_app):
    user_payload = {"username": "denise", "email": "denise@example.com", "password": "123456"}
    resp = test_app.post('/users/', json=user_payload)
    user_id = resp.json()["id"]

    response = test_app.delete(f'/users/{user_id}')
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "User successfully deleted"


# authentication tests

def test_register_and_login(test_app):
    payload = {"username": "eve", "email": "eve@example.com", "password": "secret"}
    resp = test_app.post('/auth/register', json=payload)
    assert resp.status_code == 200
    # login via username
    login_resp = test_app.post('/auth/login', json={"username": "eve", "password": "secret"})
    assert login_resp.status_code == 200
    token_data = login_resp.json()
    assert "access_token" in token_data and token_data["token_type"] == "bearer"
    token = token_data["access_token"]

    # get current user
    headers = {"Authorization": f"Bearer {token}"}
    me_resp = test_app.get('/auth/me', headers=headers)
    assert me_resp.status_code == 200
    assert me_resp.json()["username"] == "eve"



