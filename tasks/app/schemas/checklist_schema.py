from pydantic import BaseModel


class ChecklistPost(BaseModel):
    action: str

class ChecklistPut(ChecklistPost):
    is_finished: bool

class ChecklistResponse(BaseModel):
    id: int
    action: str
    is_finished: bool

    class Config:
        orm_mode = True