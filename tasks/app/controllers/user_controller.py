from fastapi import APIRouter, Depends, HTTPException, Response
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserResponse, UserPost, PasswordModify, UsernameModify
from app.services.user_service import UserService
from app.exceptions.user_exception import UserNotFound, UsernameAlreadyAssigned


user_controller = APIRouter(
    prefix="/user",
    tags=["users"])



@user_controller.get("/", response_model=list[UserResponse])
def get_all_user(db: Session = Depends(get_db)):
    return UserService(db=db).find_all_user()

@user_controller.get("/{user_id}", response_model=UserResponse, status_code=200, responses={404:{}})
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return UserService(db=db).find_user(user_id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")


@user_controller.post("/", response_model=UserResponse, status_code=200, responses={409:{}})
def create_user(user_post: UserPost, db: Session = Depends(get_db)):
    try:
        return UserService(db=db).create_user(user_post)
    except UsernameAlreadyAssigned:
        raise HTTPException(status_code=409, detail="Username already registered")

@user_controller.patch("/username/{user_id}", response_model=UserResponse, status_code=200, responses={404:{}, 409:{}})
def modify_username(user_id: int, username: UsernameModify, db: Session = Depends(get_db)):
    try:
        return UserService(db=db).modify_username(user_id, username)
    except UsernameAlreadyAssigned:
        raise HTTPException(status_code=409, detail="Username already registered")
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")


@user_controller.patch("/password/{user_id}", response_model=UserResponse, status_code=200, responses={404:{}, 409:{}})
def modify_password(user_id: int, password: PasswordModify, db: Session = Depends(get_db)):
    try:
        return UserService(db=db).modify_password(user_id, password)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")


@user_controller.delete("/{user_id}", status_code=204, responses={204:{}, 404:{}})
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        UserService(db=db).delete_user(user_id)
        return Response(status_code=204)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")