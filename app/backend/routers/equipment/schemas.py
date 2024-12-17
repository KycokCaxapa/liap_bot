from pydantic import BaseModel
from typing import Optional


class SEquipmentPost(BaseModel):
    thing: str
    amount: int
    auditorium: str


class SEquipmentGet(SEquipmentPost):
    id: int
    booked_by: Optional[int]


class SEquipmentGetForAuditorium(BaseModel):
    thing: str
    amount: int
    auditorium: int


class SEquipmentPut(SEquipmentPost):
    id: int


class SEquipmentBook(BaseModel):
    id: int
    amount: int
    booked_by: Optional[int]
