from fastapi import FastAPI, Depends
from todo_app.routers.todo import router as todo_router
from todo_app.routers.user import router as user_router
from todo_app.routers.auth import router as auth_router
from todo_app.db.connection import create_tables, get_session
from sqlmodel import Session
from typing import Annotated
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI( title="Todo List", version="1.0.0",lifespan=lifespan)

#middle
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#routers for running the app
app.include_router(todo_router)
app.include_router(user_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Welcome to dailyDo todo app"}


