from fastapi import APIRouter, Depends
from sqlmodel import Session
from todo_app.db.connection import get_session
from todo_app.schemas import auth_schemas
from todo_app.schemas.user_schemas import UserRead
from todo_app.services import auth_services

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead)
def register(user_data: auth_schemas.UserRegister, session: Session = Depends(get_session)):
    return auth_services.register_user(session, user_data)


@router.post("/login", response_model=auth_schemas.Token)
def login(credentials: auth_schemas.UserLogin, session: Session = Depends(get_session)):
    return auth_services.authenticate_user(session, credentials)


@router.get("/me", response_model=UserRead)
def read_me(current_user: UserRead = Depends(auth_services.get_current_user)):
    return current_user