from fastapi import APIRouter, HTTPException, status
from src.schemas.user import (
    UserRegisterSchema,
    UserLoginSchema,
    AuthResponse
)
from src.repositories.auth import AuthRepository
from pymongo.errors import DuplicateKeyError

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED
)
async def register(payload: UserRegisterSchema):
    exists = await AuthRepository.get_by_email(payload.email)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    try:
        data = await AuthRepository.create_user(
            email=payload.email,
            password=payload.password
        )
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    return data

@router.post("/login",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED
)
async def login(payload: UserLoginSchema):
    data = await AuthRepository.authenticate(
        email=payload.email,
        password=payload.password
    )

    if not data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    return data