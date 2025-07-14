from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Your DATABASE_URL from .env
from dotenv import load_dotenv
import os

from sqlalchemy.orm import declarative_base

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ This must be here!
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
