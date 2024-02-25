from fastapi import APIRouter
from sqlalchemy import select

from database import session
from schemas.tasks import TaskAdd, TaskUpdate
from models.models import Task


router = APIRouter()


@router.post('/add')
def task_add(task_data: TaskAdd):
    try:
        data = Task(uuid=task_data.uuid, task=task_data.task, param_1=task_data.params[0].param_1, param_2=task_data.params[0].param_2)
        session.add(data)
        session.commit()
        return {"statuscode:": 200}
    finally:
        session.close()


@router.get("/")
def task_get():
    try:
        tasks_all = session.query(Task).all()
        return tasks_all
    finally:
        session.close()


@router.put("/{uuid}")
def task_update(new_data: TaskUpdate):
    try:
        statement = select(Task).filter_by(uuid=str(new_data.uuid))
        old_data = session.execute(statement).scalar()
        old_data.task = new_data.new_task
        old_data.param_1 = new_data.new_params[0].param_1
        old_data.param_2 = new_data.new_params[0].param_2
        session.commit()
    except:
        session.rollback()

    finally:
        session.close()
