from pydantic import BaseModel
from datetime import datetime
import enum

class UserPost(BaseModel):
    username: str
    password: str


class UsernameModify(BaseModel):
    username: str


class PasswordModify(BaseModel):
    password: str

class UserResponse(BaseModel):
    id: int
    username: str


class ChecklistPost(BaseModel):
    action: str

class ChecklistPut(ChecklistPost):
    is_finished: bool

class ChecklistResponse(BaseModel):
    id: int
    action: str
    is_finished: bool

class PriorityEnum(enum.Enum):
    low = 0
    medium = 1
    high = 2


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




