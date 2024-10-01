from pydantic import BaseModel


class SEquipment(BaseModel):
    thing: str
    auditorium_id: int
