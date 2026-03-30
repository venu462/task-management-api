from typing import Optional

from sqlalchemy.orm import Session
from app.models.task_model import Task, TaskStatus
from app.schemas.task_schema import TaskCreate, TaskUpdate
import uuid


def create_task(db: Session, task: TaskCreate, user_id: uuid.UUID):
    db_tasks = Task(
        title= task.title,
        description= task.description,
        status= task.status,
        due_date= task.due_date,
        owner_id= user_id
    )
    db.add(db_tasks)
    db.commit()
    db.refresh(db_tasks)
    return db_tasks 

def get_tasks(
        db: Session, 
        user_id: uuid.UUID,
        status: Optional[TaskStatus] = None,
        skip: int = 0,
        limit: int = 10):
    query = db.query(Task).filter(Task.owner_id == user_id)
    if status:
        query = query.filter(Task.status == status)
    return query.offset(skip).limit(limit).all()

def get_task(db: Session, task_id: uuid.UUID, user_id: uuid.UUID):
    return db.query(Task).filter(
        Task.id == task_id, 
        Task.owner_id == user_id
        ).first()

def update_task(db: Session, task_id: uuid.UUID, task_update: TaskUpdate, user_id: uuid.UUID):
    task = get_task(db, task_id, user_id)
    if not task:
        return None
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: uuid.UUID, user_id: uuid.UUID):
    task = get_task(db, task_id, user_id)
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task