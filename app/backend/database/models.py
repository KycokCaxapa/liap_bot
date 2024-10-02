from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Annotated, List

from database.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base):
    __tablename__ = 'users'

    id: Mapped[intpk]
    tg_id = mapped_column(BigInteger)
    password: Mapped[str] = mapped_column(default=None, nullable=True)
    role: Mapped[str]


class Auditorium(Base):
    __tablename__ = 'auditoriums'

    id: Mapped[intpk]
    number: Mapped[str]
    members: Mapped[int]
    projector: Mapped[bool]
    equipment: Mapped[List['Equipment'] | None] = relationship(back_populates='auditorium', lazy='joined')
    '''Только с lazy='joined' при получении аудитории отображаются записи из таблицы equipments'''


class Equipment(Base):
    __tablename__ = 'equipment'

    id: Mapped[intpk]
    thing: Mapped[str]
    amount: Mapped[int]
    auditorium_id: Mapped[int] = mapped_column(ForeignKey('auditoriums.id'))
    auditorium: Mapped['Auditorium'] = relationship(back_populates='equipment')
