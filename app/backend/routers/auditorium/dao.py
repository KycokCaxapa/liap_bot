from typing import List, Optional
from sqlalchemy import select

from routers.auditorium.filters import AuditoriumFilter
from database.models import Auditorium, Equipment
from database.database import async_session
from database.base import BaseDAO


class AuditoriumDAO(BaseDAO):
    model = Auditorium
    
    async def get_by_filters(filter: AuditoriumFilter) -> Optional[List[Auditorium]]:
        async with async_session() as session:
            auditoriums = await session.execute(filter.filter(select(Auditorium)))
            return auditoriums.unique().scalars()
