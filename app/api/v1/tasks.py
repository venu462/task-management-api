from typing import Optional
import uuid

from fastapi import APIRouter, status, HTTPException, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.database import get_db
from app.crud import task as task_crud
from app.models.user_model import Users
from app.schemas.task_schema import TaskCreate, TaskResponse, TaskStatus, TaskUpdate


router = APIRouter()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    return task_crud.create_task(db, task, current_user.id)

@router.get("/", response_model=list[TaskResponse])
def get_tasks_endpoint(
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user),
    status: Optional[TaskStatus] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1)
):
    return task_crud.get_tasks(db, current_user.id, status, skip, limit)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task_endpoint(
    task_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    task = task_crud.get_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: uuid.UUID,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    task = task_crud.update_task(db, task_id, task_update, current_user.id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task(
    task_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user: Users = Depends(get_current_user)
):
    task = task_crud.delete_task(db, task_id, current_user.id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task 