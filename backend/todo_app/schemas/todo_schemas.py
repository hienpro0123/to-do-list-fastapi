from sqlmodel import SQLModel, Field

class Todo(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    content: str = Field(index=True, min_length=3, max_length=100)
    is_completed: bool = Field(default=False)
    user_id: int = Field(foreign_key="user.id", index=True)

class TodoRead(SQLModel):
    id: int | None
    content: str
    is_completed: bool