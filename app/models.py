from sqlmodel import Column, Field, String, SQLModel
from typing import Optional

class User(SQLModel, table=True):  # Add `table=True` to make this a table model
    id: Optional[int] = Field(default=None, primary_key=True, index=True)  # Explicit type annotation and `Field`
    username: str = Field(sa_column=Column(String(50), unique=True))  # Use `Field` for SQLAlchemy compatibility


class Post(SQLModel, table=True):  # Add `table=True` to make this a table model
    id: Optional[int] = Field(default=None, primary_key=True, index=True)  # Explicit type annotation and `Field`
    title: str = Field(max_length=50)  # SQLModel supports `max_length`
    content: str = Field(max_length=100)  # Explicit `max_length` for better control
    user_id: int = Field(foreign_key="user.id")  # Define a foreign key