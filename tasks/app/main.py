from fastapi import FastAPI
from app.models import user, task, checklist
from app.config.database import engine
from app.controllers import user_controller, task_controller, checklist_controller

app = FastAPI()

user.Base.metadata.create_all(bind=engine)
task.Base.metadata.create_all(bind=engine)
checklist.Base.metadata.create_all(bind=engine)


app.include_router(user_controller.user_controller)
app.include_router(task_controller.task_controller)
app.include_router(checklist_controller.checklist_controller)