from sqlmodel import SQLModel, create_engine, Session
from todo_app.db import setting

connection_string = str(setting.DATABASE_URL).replace(
    "postgresql", "postgresql+psycopg"
)

engine = create_engine(
    connection_string,
    echo=True
)

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

