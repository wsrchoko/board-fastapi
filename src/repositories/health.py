from src.database import mongo

async def check_db_health():
    await mongo.db.command("ping")
    return {"status": "ok"}