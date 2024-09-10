from sqlalchemy import insert, select, update

from app.database.database import async_session


class BaseDAO:
    model = None

    @classmethod
    async def create(cls, **data) -> None:
        async with async_session() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_by_filter(cls, **filter):
        async with async_session() as session:
            object = await session.scalar(select(cls.model).filter_by(**filter))
            return object
    
    @classmethod
    async def update_by_id(cls, id: int, **data) -> None:
        async with async_session() as session:
            await session.execute(update(cls.model).where(cls.model.id == id).values(**data))
            await session.commit()

    @classmethod
    async def delete_by_filter(cls, **filter) -> None:
        async with async_session() as session:
            object = await session.scalar(select(cls.model).filter_by(**filter))
            await session.delete(object)
            await session.commit()
