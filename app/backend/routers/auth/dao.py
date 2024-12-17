from database.database import async_session
from database.base import BaseDAO
from database.models import User
from sqlalchemy import select


class UserDAO(BaseDAO):
    model = User

    async def user_exists(tg_id: int) -> bool:
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            return user
        
    async def get_id_by_tg_id(tg_id: int) -> int:
        async with async_session() as session:
            user_id = await session.scalar(select(User.id).where(User.tg_id == tg_id))
            return user_id
    
    async def get_tg_id_by_id(id: int) -> int:
        async with async_session() as session:
            user_tg_id = await session.scalar(select(User.tg_id).where(User.id == id))
            return user_tg_id
    
    async def get_user_role(tg_id: int) -> str:
        async with async_session() as session:
            user_role = await session.scalar(select(User.role).where(User.tg_id == tg_id))
            return user_role
