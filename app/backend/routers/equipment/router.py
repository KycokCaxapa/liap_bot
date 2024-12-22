from fastapi_filter import FilterDepends
from typing import List, Optional
from fastapi import APIRouter

from routers.equipment.filters import EquipmentFilter
from routers.auditorium.dao import AuditoriumDAO
from routers.equipment.dao import EquipmentDAO
from routers.equipment.schemas import *
from routers.equipment.codes import *
from routers.auth.dao import UserDAO
from core.bot import bot


router = APIRouter(prefix='/equipment',
                   tags=['Equipment'])


@router.post('/create')
async def create_equipment(tg_id: int, data: SEquipmentPost):
    auditorium_id = await AuditoriumDAO.get_id_by_number(data.auditorium)
    if not auditorium_id:
        raise NOT_FOUND_404
    elif await EquipmentDAO.is_exists(await EquipmentDAO.get_id_by_thing(data.thing)):
        raise ALREADY_EXISTS_409
    else:
        await EquipmentDAO.create(thing=data.thing,
                                  amount=data.amount,
                                  auditorium_id=auditorium_id,
                                  booked_by=None)
        await bot.send_message(chat_id=tg_id,
                               text=f'Вы создали оборудование {data.thing}')


@router.get('/get_by_filters')
async def get_equipment_by_filters(filters: EquipmentFilter = FilterDepends(EquipmentFilter)) -> Optional[List[SEquipmentGet]]:
    equipments = await EquipmentDAO.get_by_filters(filters)
    response = [SEquipmentGet(id=equipment.id,
                             thing=equipment.thing,
                             amount=equipment.amount,
                             auditorium=equipment.auditorium.number,
                             booked_by=await UserDAO.get_tg_id_by_id(equipment.booked_by))
               for equipment in equipments]
    return response


@router.put('/update')
async def update_equipment(tg_id: int, data: SEquipmentPut) -> None:
    auditorium_id = await AuditoriumDAO.get_id_by_number(data.auditorium)
    await EquipmentDAO.update_by_id(id=data.id,
                                    thing=data.thing,
                                    amount=data.amount,
                                    auditorium_id=auditorium_id)
    await bot.send_message(chat_id=tg_id,
                           text=f'Вы изменили оборудование {data.thing}')


@router.put('/book')
async def update_equipment(tg_id: int, data: SEquipmentBook) -> None:
    print(data.model_dump_json())
    user_id = await UserDAO.get_id_by_tg_id(data.booked_by)
    equipment_thing = await EquipmentDAO.get_thing_by_id(data.id)
    message = f'Вы забронировали оборудование {equipment_thing}' if data.booked_by else f'Вы сняли бронь с оборудования {equipment_thing}'

    if data.amount < 0:
        raise UNAVAILABLE_409
    await EquipmentDAO.update_by_id(id=data.id,
                                    amount=data.amount,
                                    booked_by=user_id)
    await bot.send_message(chat_id=tg_id,
                           text=message)


@router.delete('/delete')
async def delete_equipment(tg_id: int, id: int) -> None:
    equipment_thing = await EquipmentDAO.get_thing_by_id(id)

    await EquipmentDAO.delete_by_filter(id=id)
    await bot.send_message(chat_id=tg_id,
                           text=f'Вы удалили аудиторию {equipment_thing}')
