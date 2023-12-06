from fastapi import APIRouter, HTTPException, Response
import requests
from app.schemas.tasks_schema import UserResponse, UserPost, UsernameModify, PasswordModify, TaskResponse, TaskPost, \
    TaskPut, ChecklistResponse, ChecklistPut, ChecklistPost
import json

tasks_controller = APIRouter(
    prefix="/tasks_api",
    tags=["tasks_api"])


@tasks_controller.get("/user/", response_model=list[UserResponse], status_code=200)
def get_all_users():

    response = requests.get('http://host.docker.internal:8081/user/')
    return response.json()


@tasks_controller.post("/user/", response_model=UserResponse, status_code=200, responses={409: {}})
def create_user(user: UserPost):
    response = requests.post('http://host.docker.internal:8081/user/', json={'username': user.username, 'password': user.password})

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 409:
        raise HTTPException(status_code=409, detail="Username already registered")


@tasks_controller.get("/user/{user_id}", response_model=UserResponse, status_code=200, responses={404: {}})
def get_single_user(user_id: int):
    response = requests.get(f'http://host.docker.internal:8081/user/{user_id}')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")


@tasks_controller.delete("/user/{user_id}", status_code=204, responses={404: {}})
def delete_user(user_id: int):
    response = requests.delete(f'http://host.docker.internal:8081/user/{user_id}')
    if response.status_code == 204:
        return Response(status_code=204)
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")


@tasks_controller.patch("/user/username/{user_id}",
                        response_model=UserResponse, status_code=200, responses={404: {}, 409: {}})
def modify_username(user_id: int, username: UsernameModify):
    response = requests.patch(f'http://host.docker.internal:8081/user/username/{user_id}', json={'username': username.username})
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")
    elif response.status_code == 409:
        raise HTTPException(status_code=409, detail="Username already registered")


@tasks_controller.patch("/user/password/{user_id}",
                        response_model=UserResponse, status_code=200, responses={404: {}})
def modify_password(user_id: int, password: PasswordModify):
    response = requests.patch(f'http://host.docker.internal:8081/user/password/{user_id}', json={'password': password.password})
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")


@tasks_controller.get("/user/{user_id}/tasks", response_model=list[TaskResponse], status_code=200)
def get_all_tasks_of_user(user_id: int):
    response = requests.get(f'http://host.docker.internal:8081/task/?user_id={user_id}')

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")


@tasks_controller.post("/user/{user_id}/tasks", response_model=TaskResponse, status_code=200)
def create_task_for_user(user_id: int, task_post: TaskPost):
    response = requests.post(f'http://host.docker.internal:8081/task/?user_id={user_id}',
                             json={
                                 "title": task_post.title,
                                 "description": task_post.description,
                                 "creation_date": task_post.creation_date.isoformat(),
                                 "finalization_date": task_post.finalization_date.isoformat(),
                                 "priority": task_post.priority.value

                             })

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="User not found")


@tasks_controller.get("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
def get_single_task(task_id: int):
    response = requests.get(f'http://host.docker.internal:8081/task/{task_id}')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Task not found")


@tasks_controller.put("/tasks/{task_id}", response_model=TaskResponse, status_code=200)
def modify_taks(task_id: int, task_put: TaskPut):
    response = requests.put(f'http://host.docker.internal:8081/task/{task_id}',
                            json={
                                "title": task_put.title,
                                "description": task_put.description,
                                "creation_date": task_put.creation_date.isoformat(),
                                "finalization_date": task_put.finalization_date.isoformat(),
                                "priority": task_put.priority.value,
                                "is_finished": task_put.is_finished

                            })

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Task not found")


@tasks_controller.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    response = requests.delete(f'http://host.docker.internal:8081/task/{task_id}')
    if response.status_code == 204:
        return Response(status_code=204)
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Task not found")


@tasks_controller.patch("/tasks/{task_id}", status_code=200, response_model=TaskResponse)
def modify_finish_task(task_id: int, is_finished: bool):
    response = requests.patch(f'http://host.docker.internal:8081/task/{task_id}?is_finished={is_finished}')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Task not found")


@tasks_controller.get("/tasks/{task_id}/checklists", status_code=200, response_model=list[ChecklistResponse])
def get_checklists_of_task(task_id: int):
    response = requests.get(f'http://host.docker.internal:8081/checklist?task_id={task_id}')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Task not found")


@tasks_controller.post("/tasks/{task_id}/checklist", status_code=200, response_model=TaskResponse)
def create_checklist(task_id: int, checklist_post: ChecklistPost):
    response = requests.post(f'http://host.docker.internal:8081/checklist/?task_id={task_id}', json={
        "action": checklist_post.action
    })
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Task not found")


@tasks_controller.put("/tasks/checklist/{checklist_id}", status_code=200, response_model=ChecklistResponse)
def modify_checklist(checklist_id, checklist_put: ChecklistPut):
    response = requests.put(f'http://host.docker.internal:8081/checklist/{checklist_id}', json={
        "action": checklist_put.action,
        "is_finished": checklist_put.is_finished
    })

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Checklist not found")


@tasks_controller.delete("/tasks/checklist/{checklist_id}", status_code=204)
def delete_checklist(checklist_id: int):
    response = requests.delete(f'http://host.docker.internal:8081/checklist/{checklist_id}')
    if response.status_code == 204:
        return Response(status_code=204)
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Checklist not found")


@tasks_controller.patch("/tasks/checklist/{checklist_id}", status_code=200, response_model=ChecklistResponse)
def modify_finish_checklist(checklist_id: int, is_finished: bool):
    response = requests.patch(f'http://host.docker.internal:8081/checklist/{checklist_id}?is_finished={is_finished}')
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise HTTPException(status_code=404, detail="Checklist not found")
