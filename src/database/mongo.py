from motor.motor_asyncio import AsyncIOMotorClient
import os

class Mongo:
    client: AsyncIOMotorClient | None = None
    db = None

mongo = Mongo()

async def connect():
    user = os.getenv("MONGO_USER")
    password = os.getenv("MONGO_PASSWORD")
    host = os.getenv("MONGO_HOST", "localhost")
    port = os.getenv("MONGO_PORT", "27017")
    db_name = os.getenv("MONGO_DB")

    mongo.client = AsyncIOMotorClient(
        f"mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource=admin"
    )
    mongo.db = mongo.client[db_name]

async def close():
    mongo.client.close()
