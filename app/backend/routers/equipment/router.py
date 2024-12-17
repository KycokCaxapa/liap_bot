from fastapi_filter import FilterDepends
from typing import List, Optional
from fastapi import APIRouter

from routers.equipment.filters import EquipmentFilter
from routers.auditorium.dao import AuditoriumDAO
from routers.equipment.dao import EquipmentDAO
from routers.equipment.schemas import *
from routers.equipment.codes import *
from routers.auth.dao import UserDAO


router = APIRouter(prefix='/equipment',
                   tags=['Equipment'])


@router.post('/create')
async def create_equipment(data: SEquipmentPost):
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


@router.get('/get_all')
async def get_all_equipment() -> Optional[List[SEquipmentGet]]:
    equipment = await EquipmentDAO.get_all()
    return equipment


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
async def update_equipment(data: SEquipmentPut) -> None:
    auditorium_id = await AuditoriumDAO.get_id_by_number(data.auditorium)
    await EquipmentDAO.update_by_id(id=data.id,
                                    thing=data.thing,
                                    amount=data.amount,
                                    auditorium_id=auditorium_id)


@router.put('/book')
async def update_equipment(data: SEquipmentBook) -> None:
    user_id = await UserDAO.get_id_by_tg_id(data.booked_by)
    if data.amount < 0:
        raise UNAVAILABLE_409
    await EquipmentDAO.update_by_id(id=data.id,
                                    amount=data.amount,
                                    booked_by=user_id)


@router.delete('/delete')
async def delete_equipment(id: int) -> None:
    await EquipmentDAO.delete_by_filter(id=id)
