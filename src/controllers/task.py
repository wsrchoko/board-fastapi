from fastapi import APIRouter, HTTPException, status
from src.schemas import CreateTaskSchema, UpdateTaskSchema, TaskResponse
from src.repositories.task import TaskRepository

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=TaskResponse, status_code=201)
async def create_task(payload: CreateTaskSchema):
    return await TaskRepository.create(payload)

@router.get("/{uuid}", response_model=TaskResponse)
async def get_task(uuid: str):
    task = await TaskRepository.get_by_uuid(uuid)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.get("/", response_model=list[TaskResponse])
async def list_tasks():
    return await TaskRepository.get_all()

@router.post("/{uuid}", response_model=TaskResponse, status_code=201)
async def update_task(uuid:str, payload: UpdateTaskSchema):
    task = await TaskRepository.update(uuid, payload)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.delete("/{uuid}", status_code=204)
async def delete_task(uuid: str):
    await TaskRepository.soft_delete(uuid)