from typing import List, Optional
from pydantic import BaseModel

from routers.equipment.schemas import SEquipment


class SAuditorium(BaseModel):
    number: str
    members: int
    projector: bool
    equipment: Optional[List[SEquipment]]
