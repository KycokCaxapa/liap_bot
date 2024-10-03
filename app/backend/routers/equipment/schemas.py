from pydantic import BaseModel


class SEquipment(BaseModel):
    thing: str
    amount: int
    auditorium_id: int
