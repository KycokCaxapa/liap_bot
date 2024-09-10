from app.database.models import Equipment
from app.database.base import BaseDAO


class EquipmentDAO(BaseDAO):
    model = Equipment
