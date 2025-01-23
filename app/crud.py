from sqlmodel import select
from .models import User, Post
from .database import get_session
from sqlalchemy.orm import Session

# Create a post
def create_post(post: Post, db: Session):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

# Delete a post by ID
def delete_post(post_id: int, db: Session):
    statement = select(Post).where(Post.id == post_id)
    post = db.exec(statement).first()
    if post:
        db.delete(post)
        db.commit()
    return post

# Read a post by ID
def get_post(post_id: int, db: Session):
    statement = select(Post).where(Post.id == post_id)
    return db.exec(statement).first()

# Create a user
def create_user(user: User, db: Session):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Get a user by ID
def get_user(user_id: int, db: Session):
    statement = select(User).where(User.id == user_id)
    return db.exec(statement).first()