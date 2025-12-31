from pydantic import BaseModel, EmailStr, Field
from datetime import datetime, timezone
from uuid import uuid4

class User(BaseModel):
    uuid: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    password: str
    active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
