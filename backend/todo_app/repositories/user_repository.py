from sqlmodel import Session, select
from todo_app.schemas.user_schemas import User


def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def get_users(session: Session):
    return session.exec(select(User)).all()


def get_user_by_id(session: Session, id: int):
    return session.exec(select(User).where(User.id == id)).first()


def get_user_by_username(session: Session, username: str):
    return session.exec(select(User).where(User.username == username)).first()


def get_user_by_email(session: Session, email: str):
    return session.exec(select(User).where(User.email == email)).first()


def delete_user(session: Session, user: User):
    session.delete(user)
    session.commit()