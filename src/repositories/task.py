from src.database.mongo import mongo
from src.models import Task
from src.schemas import CreateTaskSchema
from datetime import datetime, timezone

class TaskRepository:
    @staticmethod
    async def create(payload: CreateTaskSchema):
        task = Task(
            title=payload.title,
            description=payload.description,
            assigned_to=None,
            created_by="1",
            updated_by="1"
        )

        await mongo.db.tasks.insert_one(task.model_dump())

        return task
    
    @staticmethod
    async def get_by_uuid(uuid: str, trashed: bool = False):
        query = {"uuid": uuid}

        if not trashed:
            query["deleted_at"] = None

        return await mongo.db.tasks.find_one(query)

    @staticmethod
    async def get_all(trashed: bool = False):
        query = {}
        if not trashed:
            query["deleted_at"] = None

        return await mongo.db.tasks.find(query).to_list(100)

    @staticmethod
    async def update(uuid: str, payload: CreateTaskSchema):
        # Check if task exists
        task = await mongo.db.tasks.find_one({"uuid": uuid})
        if not task:
            return None

        data = {
            "title": payload.title,
            "description": payload.description,
            "status": payload.status,
            "assigned_to": payload.assigned_to,
            "updated_at": datetime.now(timezone.utc),
            "updated_by": "1"
        }

        await mongo.db.tasks.update_one(
            {"uuid": uuid},
            {"$set": data}
        )

        # Return updated task
        return await mongo.db.tasks.find_one({"uuid": uuid})

    @staticmethod
    async def soft_delete(uuid: str):
        await mongo.db.tasks.update_one(
            {"uuid": uuid},
            {"$set": {
                "deleted_at": datetime.now(timezone.utc),
                "deleted_by": "1"
            }}
        )
