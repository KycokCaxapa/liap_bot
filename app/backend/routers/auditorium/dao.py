from sqlalchemy.orm import joinedload
from typing import List, Optional
from sqlalchemy import select

from routers.auditorium.filters import AuditoriumFilter
from database.models import Auditorium, Equipment
from database.database import async_session
from database.base import BaseDAO


class AuditoriumDAO(BaseDAO):
    model = Auditorium
    
    async def get_id_by_number(number: str) -> Optional[int]:
        async with async_session() as session:
            auditorium_id = await session.scalar(select(Auditorium.id).where(Auditorium.number == number))
            return auditorium_id
    
    async def get_number_by_id(id: int) -> str:
        async with async_session() as session:
            auditorium_number = await session.scalar(select(Auditorium.number).where(Auditorium.id == id))
            return auditorium_number
    
    async def get_by_filters(filter: AuditoriumFilter) -> Optional[List[Auditorium]]:
        async with async_session() as session:
            query = filter.filter(select(Auditorium).options(joinedload(Auditorium.equipment).joinedload(Equipment.auditorium)))
            auditoriums = await session.execute(query)
            return auditoriums.unique().scalars()
