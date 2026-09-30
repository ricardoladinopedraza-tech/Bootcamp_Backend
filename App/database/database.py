from dotenv import load_dotenv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace(
        "postgresql://",
        "postgresql+psycopg://",
        1
    )

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass