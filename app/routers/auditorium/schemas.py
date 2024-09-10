from pydantic import BaseModel
from typing import List

from app.routers.equipment.schemas import SEquipment


class SAuditorium(BaseModel):
    number: str
    equipment: List[SEquipment] | None
