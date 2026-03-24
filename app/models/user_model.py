#
from sqlalchemy import Column, String, Boolean, DateTime
from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func


class Users(Base):
    __tablename__="users"

    id=Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email=Column(String, unique=True, nullable=False, index=True)
    hashed_password=Column(String, nullable=False)
    is_active=Column(Boolean, default=True)
    created_at=Column(DateTime(timezone=True), server_default=func.now())

    tasks=relationship("Task", back_populates="owner")
