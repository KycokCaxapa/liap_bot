from typing import List, Optional
from pydantic import BaseModel

from routers.equipment.schemas import SEquipmentGetForAuditorium


class SAuditoriumPost(BaseModel):
    number: str
    members: int
    projector: bool


class SAuditoriumGet(SAuditoriumPost):
    id: int
    equipment: Optional[List[SEquipmentGetForAuditorium]]
    is_booked: bool
    booked_by: Optional[int]


class SAuditoriumPut(SAuditoriumPost):
    id: int


class SAuditoriumBook(BaseModel):
    id: int
    is_booked: bool
