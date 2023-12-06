from fastapi import APIRouter, Depends, HTTPException, Response
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.services.task_service import TaskService
from app.schemas.task_schema import TaskPost, TaskResponse, TaskPut
from app.exceptions.user_exception import UserNotFound
from app.exceptions.task_exception import TaskNotFound

task_controller = APIRouter(
    prefix="/task",
    tags=["tasks"])

@task_controller.post("/", status_code=200, responses={404:{}}, response_model=TaskResponse)
def create_task(user_id: int, taskPost:TaskPost, db: Session = Depends(get_db)):
    try:
        return TaskService(db).create_task(user_id, taskPost)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")

@task_controller.put("/{task_id}", status_code=200, responses={404:{}}, response_model=TaskResponse)
def modify_task(task_id: int, taskPut: TaskPut, db: Session = Depends(get_db)):
    try:
        return TaskService(db).modify_task(task_id, taskPut)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")

@task_controller.get("/", status_code=200, responses={404:{}}, response_model=list[TaskResponse])
def get_tasks_user(user_id:int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).find_all_tasks_by_user(user_id)
    except UserNotFound:
        raise HTTPException(status_code=404, detail="User not found")

@task_controller.get("/{task_id}", status_code=200, responses={404:{}}, response_model=TaskResponse)
def get_task(task_id:int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).find_task(task_id)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")


@task_controller.patch("/{task_id}", status_code=200, responses={404:{}}, response_model=TaskResponse)
def modify_finish(is_finished: bool, task_id: int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).modify_finish_task(task_id, is_finished)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")


@task_controller.delete("/{task_id}", status_code=200, responses={404:{}}, response_model=list[TaskResponse])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).delete_task(task_id)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")