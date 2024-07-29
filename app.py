from fastapi import FastAPI
from api.api_v1 import router
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from api.api_v1.router import router
from models.user_model import User
from models.todo_model import Todo

app =FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    client_db = AsyncIOMotorClient(
    settings.MONGO_CONNECTION_STRING
).todoapp
    await init_beanie(
        database=client_db,
        document_models=[
            User, 
            Todo
        ]
    )


app.include_router(
    router,
    prefix=settings.API_V1_STR
)    