from sqlmodel import Session
from todo_app.repositories import todo_repository
from todo_app.schemas.todo_schemas import Todo

def create_todo_service(session: Session, todo: Todo, user_id: int):
    todo.user_id = user_id
    return todo_repository.create_todo(session, todo)

def get_all_todos_service(session: Session, user_id: int):
    return todo_repository.get_all_todos_by_user(session, user_id)

def get_single_todo_service(session: Session, id: int, user_id: int):
    return todo_repository.get_todo_by_id_and_user(session, id, user_id)

def delete_todo_service(session: Session, todo):
    return todo_repository.delete_todo(session, todo)