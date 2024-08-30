from pydantic import BaseModel,Field
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime

class TodoCreate(BaseModel):
     todo_id: UUID = Field(default_factory=uuid4, unique=True)
     title: str = Field(...,title='Titulo',min_length=3,max_length=50)
     status: Optional[bool] = False

class TodoUpdate(BaseModel):
     title: Optional[str]
     description: Optional[bool]
     status: Optional[bool] = False

class TodoDetail(BaseModel):
     todo_id: UUID
     status: bool
     title: str
     description: str
     created_at: datetime
     updated_at: datetime
