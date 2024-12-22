from fastapi_filter import FilterDepends
from typing import List, Optional
from fastapi import APIRouter

from routers.auditorium.filters import AuditoriumFilter
from routers.auditorium.dao import AuditoriumDAO
from routers.auditorium.schemas import *
from routers.auth.dao import UserDAO
from core.bot import bot


router = APIRouter(prefix='/auditorium',
                   tags=['Auditoriums'])


@router.post('/create')
async def create_auditorium(tg_id: int, data: SAuditoriumPost) -> None:
    await AuditoriumDAO.create(number=data.number,
                               members=data.members,
                               projector=data.projector,
                               is_booked=False,
                               booked_by=None)
    await bot.send_message(chat_id=tg_id,
                           text=f'Вы создали аудиторию {data.number}')


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
async def update_auditorium(tg_id: int, data: SAuditoriumPut) -> None:
    auditorium_number = await AuditoriumDAO.get_number_by_id(data.id)

    await AuditoriumDAO.update_by_id(id=data.id,
                                     number=data.number,
                                     members=data.members,
                                     projector=data.projector)
    await bot.send_message(chat_id=tg_id,
                           text=f'Вы изменили аудиторию {auditorium_number}')


@router.put('/book')
async def book_auditorium(tg_id: int, data: SAuditoriumBook) -> None:
    user_id = await UserDAO.get_id_by_tg_id(tg_id) if data.is_booked else None
    auditorium_number = await AuditoriumDAO.get_number_by_id(data.id)
    message = f'Вы забронировали аудиторию {auditorium_number}' if data.is_booked else f'Вы сняли бронь с аудитории {auditorium_number}'

    await AuditoriumDAO.update_by_id(id=data.id,
                                     is_booked=data.is_booked,
                                     booked_by=user_id)
    await bot.send_message(chat_id=tg_id,
                           text=message)


@router.delete('/delete')
async def delete_auditorium(tg_id: int, id: int) -> None:
    auditorium_number = await AuditoriumDAO.get_number_by_id(id)

    await AuditoriumDAO.delete_by_filter(id=id)
    await bot.send_message(chat_id=tg_id,
                           text=f'Вы удалили аудиторию {auditorium_number}')
