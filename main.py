from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import SessionLocal
from config.database import Base, engine
from src.schema.schema import TodoCreate, Todo as TodoSchema
from src.models.model import Todo

# created table at run
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for db session
def connect_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # after usage closing db connection
        db.close()

# POST - Create todo

@app.post("/create", response_model=TodoSchema)
def create(todo: TodoCreate, db: Session = Depends(connect_db)):
    db_todo = Todo(**todo.dict())
    # gets json request and converts the dict to db column for mapping and storing

    db.add(db_todo)
    db.commit()
    # add to memory with add and on commits stores in db

    db.refresh(db_todo)
    # refreshes the db and gets id from db

    # TodoSchema converts the model and returns in json
    return db_todo

# GET - fetch all todo

@app.get("/get-todos", response_model=list[TodoSchema])
def get_all(db: Session = Depends(connect_db)):
    return db.query(Todo).all()

# GET - fetch by id

@app.get("/get-todos/{todo_id}", response_model=TodoSchema)
def get_by_id(todo_id:int, db: Session = Depends(connect_db)):
    # get first data or none if not exist from todo table
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail={"message": "id not found"})
    return todo


# GET - get by status

@app.get("/get-by-status", response_model=list[TodoSchema])
def get_by_status(status:bool, db: Session = Depends(connect_db)):
    # get first data or none if not exist from todo table
    todo = db.query(Todo).filter(Todo.completion == status)
    if not todo:
        return []
    return todo


# PUT - update with id
@app.put("/update/{todo_id}", response_model=TodoSchema)
def update_by_id(todo_id:int, updated:TodoCreate, db: Session = Depends(connect_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail={"message": "task not found"})
    for key, value in updated.dict().items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo


# PUT - update with id
@app.delete("/delete/{todo_id}",)
def delete_by_id(todo_id:int, db: Session = Depends(connect_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail={"message": "task not found"})
    db.delete(todo)
    db.commit()
    return {"message": "deletion successful"}