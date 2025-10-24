from pydantic import BaseModel

# for conversion of json to python object and python object to json
class TodoBase(BaseModel):
    title: str
    description: str | None = ""
    completion: bool = False

# only when creation
class TodoCreate(TodoBase):
    pass

# for response
class Todo(TodoBase):
    id: int
    class Config:
        orm_mode = True
        # for returning in json format