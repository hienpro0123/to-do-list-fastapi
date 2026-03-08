from sqlmodel import Session
from todo_app.repositories import user_repository
from todo_app.schemas.user_schemas import User


def create_user_service(session: Session, user: User):
    return user_repository.create_user(session, user)


def get_all_users_service(session: Session):
    return user_repository.get_users(session)


def get_single_user_service(session: Session, id: int):
    return user_repository.get_user_by_id(session, id)


def get_user_by_username_service(session: Session, username: str):
    return user_repository.get_user_by_username(session, username)


def get_user_by_email_service(session: Session, email: str):
    return user_repository.get_user_by_email(session, email)


def delete_user_service(session: Session, user: User):
    return user_repository.delete_user(session, user)