from sqlmodel import Session
from .database import get_session
from typing import Annotated
from fastapi import Depends

SessionDep = Annotated[Session, Depends(get_session)]