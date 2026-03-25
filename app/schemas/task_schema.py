from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.task_model import TaskStatus
import uuid

class TaskBase(BaseModel):
    title: str
    description: Optional[str]=None
    status: TaskStatus.todo
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
    