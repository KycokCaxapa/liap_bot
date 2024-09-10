from app.database.models import Auditorium
from app.database.base import BaseDAO


class AuditoriumDAO(BaseDAO):
    model = Auditorium
