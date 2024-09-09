from app.database.database import async_session
from app.database.base import BaseDAO
from app.database.models import User
from sqlalchemy import select


class UserDAO(BaseDAO):
    model = User

    async def user_exists(tg_id: int) -> bool:
        async with async_session() as session:
            user = await session.scalar(select(User).where(User.tg_id == tg_id))
            return user
