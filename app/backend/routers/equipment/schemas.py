from pydantic import BaseModel


class SEquipmentPost(BaseModel):
    thing: str
    amount: int
    auditorium: str


class SEquipmentGet(BaseModel):
    id: int
    thing: str
    amount: int
    auditorium: str


class SEquipmentGetForAuditorium(BaseModel):
    thing: str
    amount: int
    auditorium: int


class SEquipmentUpdate(BaseModel):
    id: int
    thing: str
    amount: int
    auditorium: str
