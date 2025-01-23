from sqlmodel import select
from .models import User, Post
from .dependencies import SessionDep
from sqlalchemy.orm import Session

def create_post(post: Post, db: SessionDep):
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

def delete_post(post_id: int, db: SessionDep):
    statement = select(Post).where(Post.id == post_id)
    post = db.exec(statement).first()
    if post:
        db.delete(post)
        db.commit()
    return post

def get_post(post_id: int, db: SessionDep):
    statement = select(Post).where(Post.id == post_id)
    return db.exec(statement).first()

def create_user(user: User, db: SessionDep):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(user_id: int, db: SessionDep):
    statement = select(User).where(User.id == user_id)
    return db.exec(statement).first()