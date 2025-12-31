from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone
from uuid import uuid4
from .enum.task_status import TaskStatus


class Task(BaseModel):
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: str
    status: TaskStatus = TaskStatus.pending

    assigned_to: Optional[str] = None

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    created_by: str

    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str

    deleted_at: Optional[datetime] = None
    deleted_by: Optional[str] = None
