from pydantic import BaseModel

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

    class Config:
        orm_mode = True