from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

from app.database.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    tg_id = mapped_column(BigInteger)
    password: Mapped[str]
    role: Mapped[str]


class Auditorium(Base):
    __tablename__ = 'auditorium'

    id: Mapped[intpk]


class Equipment(Base):
    __tablename__ = 'equipment'

    id: Mapped[intpk]
