from sqlalchemy.orm import selectinload, joinedload
from typing import List, Optional
from sqlalchemy import select

from routers.equipment.filters import EquipmentFilter
from database.database import async_session
from database.models import Auditorium, Equipment
from database.base import BaseDAO


class EquipmentDAO(BaseDAO):
    model = Equipment

    async def get_id_by_thing(thing: str) -> int:
        async with async_session() as session:
            equipment_id = await session.scalar(select(Equipment.id).where(Equipment.thing == thing))
            return equipment_id

    async def get_thing_by_id(id: int) -> str:
        async with async_session() as session:
            equipment_thing = await session.scalar(select(Equipment.thing).where(Equipment.id == id))
            return equipment_thing
    
    async def get_auditorium_by_id(id: int) -> str:
        async with async_session() as session:
            auditorium = await session.scalar(select(Auditorium.number).where(Auditorium.id == id))
            return auditorium

    async def get_by_filters(filter: EquipmentFilter) -> Optional[List[Equipment]]:
        async with async_session() as session:
            query = filter.filter(select(Equipment).options(joinedload(Equipment.auditorium)))
            equipment = await session.execute(query)
            return equipment.unique().scalars()
