from sqlmodel import Session
from todo_app.repositories import todo_repository
from todo_app.schemas.todo_schemas import Todo

def create_todo_service(session: Session, todo: Todo):
    return todo_repository.create_todo(session, todo)

def get_all_todos_service(session: Session):
    return todo_repository.get_all_todos(session)

def get_single_todo_service(session: Session, id: int):
    return todo_repository.get_todo_by_id(session, id)

def delete_todo_service(session: Session, todo):
    return todo_repository.delete_todo(session, todo)