from datetime import datetime

from fastapi import HTTPException
from models.user_model import User
from models.todo_model import Todo
from typing import List
from schemas.todo_schema import TodoCreate, TodoUpdate
from uuid import UUID

class TodoService:
    @staticmethod
    async def list_todos(user: User) -> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.id).to_list()
        return todos
    
    @staticmethod
    async def create_todo(user: User, data: TodoCreate) -> Todo:
        todo = Todo(**data.dict(), owner=user)
        return await todo.insert()
    
    @staticmethod
    async def detail(user: User, todo_id: UUID):
        todo = await Todo.find_one(Todo.todo_id == todo_id, Todo.owner.id == user.id)
        return todo
    
    
    @staticmethod
    async def update_todo(user: User, todo_id: UUID, data: TodoUpdate):
        todo = await TodoService.detail(user, todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
            update_data = data.dict(exclude_unset=True)
            update_data["updated_at"] = datetime.utcnow()  # Atualize o campo updated_at
            await todo.update({"$set": update_data})
            await todo.save()
            return todo

    
    @staticmethod
    async def delete_todo(user: User, todo_id: UUID) -> None:
        todo = await TodoService.detail(user, todo_id)
        if todo:
            await todo.delete()
        return None