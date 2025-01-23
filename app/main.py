from fastapi import FastAPI, HTTPException, Depends, status
from .models import User, Post
from .schemas import PostBase, UserBase
from .crud import create_post, delete_post, get_post, create_user, get_user
from .database import create_db_and_tables, get_session
from .dependencies import SessionDep

async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post_endpoint(post: PostBase, db: SessionDep):
    db_post = Post(**post.model_dump())
    return create_post(db_post, db)

@app.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post_endpoint(post_id: int, db: SessionDep):
    post = delete_post(post_id, db)
    if post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return {"message": "Post deleted successfully"}

@app.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: SessionDep):
    post = get_post(post_id, db)
    if post is None:
        raise HTTPException(status_code=404, detail='Post not found')
    return post

@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user_endpoint(user: UserBase, db: SessionDep):
    db_user = Post(**user.model_dump())
    return create_user(db_user, db)

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: SessionDep):
    user = get_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found')
    return user