from typing import List, Optional
from sqlalchemy import select

from routers.equipment.filters import EquipmentFilter
from database.database import async_session
from database.models import Equipment
from database.base import BaseDAO


class EquipmentDAO(BaseDAO):
    model = Equipment

    async def get_by_filters(filter: EquipmentFilter) -> Optional[List[Equipment]]:
        async with async_session() as session:
            equipment = await session.scalars(filter.filter(select(Equipment)))
            return equipment
