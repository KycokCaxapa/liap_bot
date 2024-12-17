from pydantic import BaseModel
from typing import Optional


class SUser(BaseModel):
    tg_id: int
    username: str
    role: str
    auditoriums: Optional[int]
    equipment: Optional[int]
