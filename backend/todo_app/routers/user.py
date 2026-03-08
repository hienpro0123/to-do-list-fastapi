from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from sqlmodel import Session, select
from todo_app.db.connection import get_session
from todo_app.schemas.user_schemas import User, UserRead
from todo_app.schemas import auth_schemas
from todo_app.services import user_services
from todo_app.services import auth_services

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
def create(user_data: auth_schemas.UserRegister, session: Annotated[Session, Depends(get_session)]):
    # hash the password before storing
    hashed = auth_services.get_password_hash(user_data.password)
    user = User(username=user_data.username, email=user_data.email, hashed_password=hashed)
    return user_services.create_user_service(session, user)


@router.get("/", response_model=list[UserRead])
def get_all(session: Annotated[Session, Depends(get_session)]):
    users = user_services.get_all_users_service(session)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.get("/{id}", response_model=UserRead)
def get_one(id: int, session: Annotated[Session, Depends(get_session)]):
    user_item = user_services.get_single_user_service(session, id)
    if not user_item:
        raise HTTPException(status_code=404, detail="User not found")
    return user_item


# DELETE
@router.delete("/{id}")
def delete(id: int, session: Annotated[Session, Depends(get_session)]):
    user = session.exec(select(User).where(User.id == id)).first()

    if not user:
        raise HTTPException(status_code=404, detail="No user found")

    session.delete(user)
    session.commit()

    return {"message": "User successfully deleted"}