from pydantic import Basemodel

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool

    class Config:
        orm_mode = True