from fastapi_filter import FilterDepends
from typing import List, Optional
from fastapi import APIRouter

from routers.auditorium.filters import AuditoriumFilter
from routers.auditorium.dao import AuditoriumDAO
from routers.auditorium.schemas import *
from routers.auth.dao import UserDAO


router = APIRouter(prefix='/auditorium',
                   tags=['Auditoriums'])


@router.post('/create')
async def create_auditorium(data: SAuditoriumPost) -> None:
    await AuditoriumDAO.create(number=data.number,
                               members=data.members,
                               projector=data.projector,
                               is_booked=False,
                               booked_by=None)


@router.get('/get_all')
async def get_all_auditoriums() -> Optional[List[SAuditoriumGet]]:
    auditorium = await AuditoriumDAO.get_all()
    return auditorium


@router.get('/get_by_filters')
async def get_auditoriums_by_filters(filters: AuditoriumFilter = FilterDepends(AuditoriumFilter)) -> Optional[List[SAuditoriumGet]]:
    auditoriums = await AuditoriumDAO.get_by_filters(filters)
    response = [
        SAuditoriumGet(
            id=auditorium.id,
            number=auditorium.number,
            members=auditorium.members,
            projector=auditorium.projector,
            equipment=[
                SEquipmentGetForAuditorium(
                    thing=equipment.thing,
                    amount=equipment.amount,
                    auditorium=equipment.auditorium_id
                ) for equipment in auditorium.equipment
            ] if auditorium.equipment else [],
            is_booked=auditorium.is_booked,
            booked_by=await UserDAO.get_tg_id_by_id(auditorium.booked_by)
        )
        for auditorium in auditoriums
    ]
    return response


@router.put('/update')
async def update_auditorium(data: SAuditoriumPut) -> None:
    await AuditoriumDAO.update_by_id(id=data.id,
                                     number=data.number,
                                     members=data.members,
                                     projector=data.projector)


@router.put('/book')
async def book_auditorium(data: SAuditoriumBook) -> None:
    user_id = await UserDAO.get_id_by_tg_id(data.tg_id)
    await AuditoriumDAO.update_by_id(id=data.id,
                                     is_booked=data.is_booked,
                                     booked_by=user_id)


@router.delete('/delete')
async def delete_auditorium(id: int) -> None:
    await AuditoriumDAO.delete_by_filter(id=id)
