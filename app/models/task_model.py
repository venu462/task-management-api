from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Enum
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
import enum

class TaskStatus(str, enum.Enum):
    todo="todo"
    in_progress="in_progress"
    done="done"

class Task(Base):
    __tablename__="tasks"

    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title=Column(String, nullable=False)
    description=Column(String, nullable=True)
    status=Column(Enum(TaskStatus), default=TaskStatus.todo, nullable=False)
    due_date=Column(DateTime(timezone=True), nullable=True)
    created_date=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True), onupdate=func.now())


owner_id= Column(UUID(as_uuid=True), ForeignKey("user_model.id"), nullable=False)
owner=relationship("User", back_populates="task")