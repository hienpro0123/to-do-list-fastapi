from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session, select
from todo_app.db.connection import get_session
from todo_app.schemas.todo_schemas import Todo
from todo_app.services import todo_services

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.post("/", response_model=Todo)
def create(todo_data: Todo, session: Annotated[Session, Depends(get_session)]):
    return todo_services.create_todo_service(session, todo_data)


@router.get("/", response_model=list[Todo])
def get_all(session: Annotated[Session, Depends(get_session)]):
    todos = todo_services.get_all_todos_service(session)
    if not todos:
        raise HTTPException(status_code=404, detail="No tasks found")
    return todos


@router.get("/{id}", response_model=Todo)
def get_one(id: int, session: Annotated[Session, Depends(get_session)]):
    todo_item = todo_services.get_single_todo_service(session, id)
    if not todo_item:
        raise HTTPException(status_code=404, detail="Task not found")
    return todo_item



# UPDATE
@router.put("/{id}", response_model=Todo)
def update(id: int, todo_data: Todo, session: Annotated[Session, Depends(get_session)]):
    existing_todo = session.exec(select(Todo).where(Todo.id == id)).first()

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
def delete(id: int, session: Annotated[Session, Depends(get_session)]):
    todo = session.exec(select(Todo).where(Todo.id == id)).first()

    if not todo:
        raise HTTPException(status_code=404, detail="No task found")

    session.delete(todo)
    session.commit()

    return {"message": "Task successfully deleted"}