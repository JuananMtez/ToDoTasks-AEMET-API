from pydantic import BaseModel
from app.schemas.checklist_schema import ChecklistResponse
from datetime import datetime
from app.models.task import PriorityEnum

class TaskPost(BaseModel):
    title: str
    description: str
    creation_date: datetime
    finalization_date: datetime
    priority: PriorityEnum

class TaskPut(TaskPost):
    is_finished: bool

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    creation_date: datetime
    finalization_date: datetime
    priority: PriorityEnum
    is_finished: bool
    checklists: list[ChecklistResponse]

    class Config:
        orm_mode = True