from app.models.task import Task
from app.models.checklist import Checklist

class TaskCrud:
    def __init__(self, db):
        self.db = db

    def find_by_id(self, id):
        return self.db.query(Task).filter(Task.id == id).first()

    def find_all_by_users(self, user_id):
        return self.db.query(Task).filter(Task.user_id == user_id).all()


    def delete_task(self, task):
        self.db.delete(task)
        self.db.commit()

    def delete_checklist(self, checklist):
        self.db.delete(checklist)
        self.db.commit()

    def save_task(self, task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def save_checklist(self, checklist):
        self.db.add(checklist)
        self.db.commit()
        self.db.refresh(checklist)
        return checklist

    def find_checklist_by_id(self, checklist_id):
        return self.db.query(Checklist).filter(Checklist.id == checklist_id).first()