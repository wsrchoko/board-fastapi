from fastapi import APIRouter
from src.repositories.health import check_db_health

router = APIRouter(
    prefix="/health",
    tags=["health"]
)

@router.get("/db")
async def health():
    return await check_db_health()
