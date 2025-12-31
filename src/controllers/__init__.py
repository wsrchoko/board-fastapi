from .health import router as health_router
from .task import router as task_router
from .auth import router as auth_router

__all__ = [
    "auth_router"
    "health_router",
    "task_router",
]
