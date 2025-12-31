from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime

class UserRegisterSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

    @field_validator("email", "password")
    @classmethod
    def strip_strings(cls, value: str):
        return value.strip()
    
class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

    @field_validator("email", "password")
    @classmethod
    def strip_strings(cls, value: str):
        return value.strip()
    
class UserResponse(BaseModel):
    uuid: str
    email: EmailStr
    created_at: datetime
    updated_at: datetime
