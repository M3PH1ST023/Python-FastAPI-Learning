from sqlalchemy import Column, Integer, String, Boolean
from config.database import Base

# model of todo

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True , index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    completion = Column(Boolean, default=False)
