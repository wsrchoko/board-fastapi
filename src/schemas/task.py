from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional
from src.models.enum.task_status import TaskStatus

class CreateTaskSchema(BaseModel):
    title: str = Field(..., min_length=4, max_length=255)
    description: str = Field(..., min_length=15, max_length=1000)
    assigned_to: Optional[str] = None

    @field_validator("title", "description")
    @classmethod
    def strip_strings(cls, value: str):
        return value.strip()

class UpdateTaskSchema(BaseModel):
    title: str = Field(..., min_length=4, max_length=255)
    description: str = Field(..., min_length=15, max_length=1000)
    status: Optional[TaskStatus] = None
    assigned_to: Optional[str] = None

    @field_validator("title", "description")
    @classmethod
    def strip_strings(cls, value: str):
        return value.strip()

class TaskResponse(BaseModel):
    uuid: str
    title: str
    description: str
    status: TaskStatus
    assigned_to: Optional[str]
    created_by: str
    created_at: datetime
    updated_by: str
    updated_at: datetime