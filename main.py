from fastapi import FastAPI, APIRouter
from contextlib import asynccontextmanager
from src.database import connect, close
from src.controllers import auth_router, health_router, task_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect()
    yield
    await close()

app = FastAPI(lifespan=lifespan)

api_v1 = APIRouter(prefix="/api/v1")

api_v1.include_router(auth_router)
api_v1.include_router(health_router)
api_v1.include_router(task_router)

app.include_router(api_v1)