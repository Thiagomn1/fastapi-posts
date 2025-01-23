import os
from dotenv import load_dotenv
from sqlmodel import create_engine

# Load environment variables from .env file
load_dotenv()

# Get the database URL from environment variables
URL_DATABASE = os.getenv('DATABASE_URL')

# Create engine with the URL from environment variable
engine = create_engine(URL_DATABASE)

def create_db_and_tables():
    from sqlmodel import SQLModel
    SQLModel.metadata.create_all(engine)

def get_session():
    from sqlmodel import Session
    with Session(engine) as session:
        yield session