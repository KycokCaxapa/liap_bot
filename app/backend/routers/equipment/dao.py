from database.models import Equipment
from database.base import BaseDAO


class EquipmentDAO(BaseDAO):
    model = Equipment
