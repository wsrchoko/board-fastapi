from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.database import connect, close
from src.controllers import health_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect()
    yield
    await close()

app = FastAPI(lifespan=lifespan)

app.include_router(health_router)