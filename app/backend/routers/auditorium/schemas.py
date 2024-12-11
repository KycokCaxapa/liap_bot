from typing import List, Optional
from pydantic import BaseModel

from routers.equipment.schemas import SEquipmentGetForAuditorium


class SAuditoriumPost(BaseModel):
    number: str
    members: int
    projector: bool


class SAuditoriumGet(BaseModel):
    id: int
    number: str
    members: int
    projector: bool
    equipment: Optional[List[SEquipmentGetForAuditorium]]


class SAuditoriumUpdate(BaseModel):
    id: int
    number: str
    members: int
    projector: bool
