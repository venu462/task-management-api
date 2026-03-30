from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.task_model import TaskStatus
import uuid
from enum import Enum

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

class TaskBase(BaseModel):
    title: str
    description: Optional[str]=None
    status: TaskStatus = TaskStatus.todo
    due_date: Optional[datetime]=None

class TaskCreate(TaskBase):
    pass 

class TaskUpdate(BaseModel):
    title: Optional[str]=None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[datetime] = None

class TaskResponse(TaskBase):
    id: uuid.UUID
    owner_id: uuid.UUID
    created_at: datetime
    update_at: Optional[datetime]=None

    model_config = {"from_attributes": True}
    