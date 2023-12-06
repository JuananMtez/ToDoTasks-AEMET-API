from app.repositories.task_crud import TaskCrud
from app.repositories.user_crud import UserCrud
from app.exceptions.user_exception import UserNotFound
from app.exceptions.task_exception import TaskNotFound, ChecklistNotFound
from app.models.task import Task
from app.models.checklist import Checklist



class TaskService:
    def __init__(self, db):
        self.task_crud = TaskCrud(db)
        self.db = db

    def create_task(self, user_id, taskPost):
        if not UserCrud(self.db).exists_by_id(user_id):
            raise UserNotFound

        db_task = Task(title=taskPost.title,
                       description=taskPost.description,
                       creation_date=taskPost.creation_date,
                       finalization_date=taskPost.finalization_date,
                       priority=taskPost.priority,
                       is_finished=False,
                       user_id=user_id,
                       checklists=[])

        return self.task_crud.save_task(db_task)

    def modify_task(self, task_id, taskPut):
        task = self.task_crud.find_by_id(task_id)
        if task is None:
            raise TaskNotFound

        task.title = taskPut.title
        task.description = taskPut.description
        task.creation_date = taskPut.creation_date
        task.finalization_date = taskPut.finalization_date
        task.priority = taskPut.priority
        task.is_finished = taskPut.is_finished

        if taskPut.is_finished:
            for checklist in task.checklists:
                checklist.is_finished = True

        return self.task_crud.save_task(task)




    def find_all_tasks_by_user(self, user_id):
        user = UserCrud(self.db).find_by_id(user_id)
        if user is None:
            raise UserNotFound

        return user.tasks

    def find_task(self, task_id):
        task = self.task_crud.find_by_id(task_id)
        if task is None:
            raise TaskNotFound

        return task

    def create_checklist(self, task_id, checklist_post):
        task = self.task_crud.find_by_id(task_id)
        if task is None:
            raise TaskNotFound

        task.checklists.append(Checklist(action=checklist_post.action,
                              is_finished=False,
                              task_id =task_id))

        return self.task_crud.save_task(task)

    def delete_checklist(self, checklist_id):
        checklist = self.task_crud.find_checklist_by_id(checklist_id)

        if checklist is None:
            raise ChecklistNotFound

        self.task_crud.delete_checklist(checklist)

        return self.task_crud.find_by_id(checklist.task_id)

    def modify_finish_checklist(self, checklist_id, is_finished):
        checklist = self.task_crud.find_checklist_by_id(checklist_id)

        if checklist is None:
            raise ChecklistNotFound

        checklist.is_finished = is_finished

        return self.task_crud.save_checklist(checklist)

    def delete_task(self, task_id):
        task = self.task_crud.find_by_id(task_id)
        if task is None:
            raise TaskNotFound

        self.task_crud.delete_task(task)
        user = UserCrud(self.db).find_by_id(task.user_id)
        return user.tasks


    def modify_finish_task(self, task_id, is_finished):
        task = self.task_crud.find_by_id(task_id)
        if task is None:
            raise TaskNotFound

        task.is_finished = is_finished

        if is_finished:
            for checklist in task.checklists:
                checklist.is_finished = True

        return self.task_crud.save_task(task)

    def get_checklist_by_task(self, task_id):
        task = self.task_crud.find_by_id(task_id)
        if task is None:
            raise TaskNotFound

        return task.checklists

    def modify_checklist(self, checklist_id, checklist_put):
        checklist = self.task_crud.find_checklist_by_id(checklist_id)

        if checklist is None:
            raise ChecklistNotFound

        checklist.action = checklist_put.action
        checklist.is_finished = checklist_put.is_finished
        checklist = self.task_crud.save_checklist(checklist)

        return checklist