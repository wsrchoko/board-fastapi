from fastapi import APIRouter, Depends, HTTPException, status
from src.schemas import CreateTaskSchema, UpdateTaskSchema, TaskResponse
from src.repositories.task import TaskRepository
from src.dependencies.auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(payload: CreateTaskSchema, user=Depends(get_current_user)):
    return await TaskRepository.create(payload)

@router.get("/{uuid}", response_model=TaskResponse)
async def get_task(uuid: str, user=Depends(get_current_user)):
    task = await TaskRepository.get_by_uuid(uuid)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.get("/", response_model=list[TaskResponse])
async def list_tasks(user=Depends(get_current_user)):
    return await TaskRepository.get_all()

@router.post("/{uuid}", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def update_task(uuid:str, payload: UpdateTaskSchema, user=Depends(get_current_user)):
    task = await TaskRepository.update(uuid, payload)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(uuid: str, user=Depends(get_current_user)):
    await TaskRepository.soft_delete(uuid)