from sqlmodel import Column, Field, String, SQLModel
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    username: str = Field(sa_column=Column(String(50), unique=True))


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    title: str = Field(max_length=50)
    content: str = Field(max_length=100)
    user_id: int = Field(foreign_key="user.id") 