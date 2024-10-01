from sqlalchemy import select
from sqlalchemy.orm import joinedload
from database.models import Auditorium, Equipment
from database.database import async_session
from database.base import BaseDAO


class AuditoriumDAO(BaseDAO):
    model = Auditorium
