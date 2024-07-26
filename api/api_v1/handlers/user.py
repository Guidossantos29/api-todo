from fastapi import APIRouter,HTTPException,status
import pymongo
from schemas.user_schema import UserAuth, UserDetail
from services.user_service import UserService


user_router = APIRouter()

@user_router.post('/adiciona',summary='adicionando usuario',response_model=UserDetail)
async def adiciona_usuario(data:UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyErrors:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Username ou email desse usuario ja existe'
        )