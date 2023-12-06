from fastapi import FastAPI
from app.controllers import aemet_controller, tasks_controller
app = FastAPI()

app.include_router(tasks_controller.tasks_controller)
app.include_router(aemet_controller.aemet_controller)
