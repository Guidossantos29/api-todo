from typing import Optional
from pydantic import BaseModel,EmailStr,Field
from uuid import UUID

class UserAuth(BaseModel):
    
        email: EmailStr = Field(...,description='email Usuario'),
        username: str = Field(...,min_length=4,max_length=50,description='username ususario'),
        password: str = Field(...,min_length=5,max_length=20,description='senha do Usuario')
    
class UserDetail(BaseModel):
        user_id: UUID
        username: str
        email: EmailStr
        first_name:Optional[str]
        last_name:Optional[str]
        disabled:Optional[bool]
