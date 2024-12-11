from pydantic import BaseModel


class SUser(BaseModel):
    tg_id: int
    username: str
    role: str
