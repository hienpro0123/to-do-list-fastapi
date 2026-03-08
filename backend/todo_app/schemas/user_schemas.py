from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True, min_length=3, max_length=32)
    email: str = Field(index=True, min_length=5, max_length=254)
    # store hashed password, never plain text
    hashed_password: str = Field(min_length=6)


class UserRead(SQLModel):
    id: int | None
    username: str
    email: str