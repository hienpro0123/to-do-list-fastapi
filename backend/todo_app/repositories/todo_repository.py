from sqlmodel import Session, select
from todo_app.schemas.todo_schemas import Todo

def create_todo(session: Session, todo: Todo):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def get_all_todos(session: Session):
    return session.exec(select(Todo)).all()

def get_todo_by_id(session: Session, id: int):
    return session.exec(select(Todo).where(Todo.id == id)).first()

def delete_todo(session: Session, todo: Todo):
    session.delete(todo)
    session.commit()