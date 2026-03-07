from fastapi import FastAPI, Depends
from todo_app.routers.todo import router as todo_router
from todo_app.db.connection import create_tables, get_session
from sqlmodel import Session
from typing import Annotated
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="dailyDo Todo App",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(todo_router)


@app.get("/")
def root():
    return {"message": "Welcome to dailyDo todo app"}


