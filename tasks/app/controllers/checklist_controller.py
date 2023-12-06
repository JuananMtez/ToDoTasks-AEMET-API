from fastapi import APIRouter, Depends, HTTPException
from app.config.database import get_db
from sqlalchemy.orm import Session
from app.services.task_service import TaskService
from app.schemas.task_schema import TaskResponse
from app.exceptions.task_exception import TaskNotFound, ChecklistNotFound
from app.schemas.checklist_schema import ChecklistPost, ChecklistResponse, ChecklistPut


checklist_controller = APIRouter(
    prefix="/checklist",
    tags=["checklists"])

@checklist_controller.post("/", status_code=200, responses={404:{}}, response_model=TaskResponse)
def create_checklist(task_id: int, checklist_post: ChecklistPost, db: Session = Depends(get_db)):
    try:
        return TaskService(db).create_checklist(task_id, checklist_post)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")

@checklist_controller.delete("/{checklist_id}", status_code=200, responses={404:{}}, response_model=TaskResponse)
def delete_checklist(checklist_id: int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).delete_checklist(checklist_id)
    except ChecklistNotFound:
        raise HTTPException(status_code=404, detail="Checklist not found")


@checklist_controller.patch("/{checklist_id}", status_code=200, responses={404:{}}, response_model=ChecklistResponse)
def modify_finish(is_finished: bool, checklist_id: int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).modify_finish_checklist(checklist_id, is_finished)
    except ChecklistNotFound:
        raise HTTPException(status_code=404, detail="Checklist not found")

@checklist_controller.get("/", status_code=200, responses={404:{}}, response_model=list[ChecklistResponse])
def get_all_checklists_by_task(task_id: int, db: Session = Depends(get_db)):
    try:
        return TaskService(db).get_checklist_by_task(task_id)
    except TaskNotFound:
        raise HTTPException(status_code=404, detail="Task not found")


@checklist_controller.put("/{checklist_id}", status_code=200, responses={404: {}}, response_model=ChecklistResponse)
def modify_checklist(checklist_id: int, checklist_put: ChecklistPut, db: Session = Depends(get_db)):
    try:
        return TaskService(db).modify_checklist(checklist_id, checklist_put)
    except ChecklistNotFound:
        raise HTTPException(status_code=404, detail="Checklist not found")
