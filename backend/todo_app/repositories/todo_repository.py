from sqlmodel import Session, select
from todo_app.schemas.todo_schemas import Todo

def create_todo(session: Session, todo: Todo):
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def get_all_todos_by_user(session: Session, user_id: int):
    return session.exec(select(Todo).where(Todo.user_id == user_id)).all()

def get_todo_by_id_and_user(session: Session, id: int, user_id: int):
    return session.exec(
        select(Todo).where(Todo.id == id, Todo.user_id == user_id)
    ).first()

def delete_todo(session: Session, todo: Todo):
    session.delete(todo)
    session.commit()