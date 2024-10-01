from pydantic import BaseModel
from typing import List

from routers.equipment.schemas import SEquipment


class SAuditorium(BaseModel):
    number: str
    equipment: List[SEquipment] | None
