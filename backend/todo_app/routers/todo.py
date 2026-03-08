from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session, select
from todo_app.db.connection import get_session
from todo_app.schemas.todo_schemas import Todo, TodoRead
from todo_app.schemas.user_schemas import User
from todo_app.services import todo_services
from todo_app.services import auth_services

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=TodoRead)
def create(
    todo_data: Todo,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(auth_services.get_current_user),
):
    return todo_services.create_todo_service(session, todo_data, current_user.id)


@router.get("/", response_model=list[TodoRead])
def get_all(
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(auth_services.get_current_user),
):
    todos = todo_services.get_all_todos_service(session, current_user.id)
    if not todos:
        raise HTTPException(status_code=404, detail="No tasks found")
    return todos


@router.get("/{id}", response_model=TodoRead)
def get_one(
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(auth_services.get_current_user),
):
    todo_item = todo_services.get_single_todo_service(session, id, current_user.id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo_item


# UPDATE
@router.put("/{id}", response_model=TodoRead)
def update(
    id: int,
    todo_data: Todo,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(auth_services.get_current_user),
):
    existing_todo = session.exec(
        select(Todo).where(Todo.id == id, Todo.user_id == current_user.id)
    ).first()

    if not existing_todo:
        raise HTTPException(status_code=404, detail="No task found")

    existing_todo.content = todo_data.content
    existing_todo.is_completed = todo_data.is_completed

    session.add(existing_todo)
    session.commit()
    session.refresh(existing_todo)

    return existing_todo


# DELETE
@router.delete("/{id}")
def delete(
    id: int,
    session: Annotated[Session, Depends(get_session)],
    current_user: User = Depends(auth_services.get_current_user),
):
    todo = session.exec(
        select(Todo).where(Todo.id == id, Todo.user_id == current_user.id)
    ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="No task found")

    session.delete(todo)
    session.commit()

    return {"message": "Task successfully deleted"}