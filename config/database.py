from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# loads environment file
load_dotenv()

# gets db connection string from env file
DATABASE_URL = os.getenv("DATABASE_URL")

# created engine
engine = create_engine(DATABASE_URL)

# session creation, autoflush to prevent auto deletion
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# for ORM
Base = declarative_base()