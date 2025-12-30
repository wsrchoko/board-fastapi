from motor.motor_asyncio import AsyncIOMotorClient
import os

class Mongo:
    client: AsyncIOMotorClient | None = None
    db = None

mongo = Mongo()

async def connect():
    mongo.client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    mongo.db = mongo.client[os.getenv("MONGO_DB")]

async def close():
    mongo.client.close()
