from src.database.mongo import mongo
from src.models import User
from src.utils.security import hash_password, verify_password
from src.utils.jwt import create_access_token

class AuthRepository:

    @staticmethod
    async def get_by_email(email: str) -> User | None:
        return await mongo.db.users.find_one({"email": email})

    @staticmethod
    async def create_user(email: str, password: str):
        user = User(
            email=email,
            password=hash_password(password)
        )

        await mongo.db.users.insert_one(user.model_dump())

        token = create_access_token({"uuid": user.uuid, "email": user.email})

        return {
            "user": user,
            "access_token": token
        }

    @staticmethod
    async def authenticate(email: str, password: str):
        user = await mongo.db.users.find_one({"email": email})

        if not user:
            return None

        if not verify_password(password, user["password"]):
            return None

        token = create_access_token({"uuid": user["uuid"], "email": user["email"]})

        return {
            "user": user,
            "access_token": token
        }
