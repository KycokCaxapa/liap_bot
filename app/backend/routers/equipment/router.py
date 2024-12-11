from fastapi_filter import FilterDepends
from fastapi import APIRouter
from typing import List, Optional

from routers.equipment.filters import EquipmentFilter
from routers.auditorium.dao import AuditoriumDAO
from routers.equipment.dao import EquipmentDAO
from routers.equipment.schemas import *
from routers.equipment.codes import *


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
                                  auditorium_id=auditorium_id)


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
                             auditorium=equipment.auditorium.number)
               for equipment in equipments]
    return response


@router.put('/update')
async def update_equipment(data: SEquipmentUpdate) -> None:
    auditorium_id = await AuditoriumDAO.get_id_by_number(data.auditorium)
    await EquipmentDAO.update_by_id(id=data.id,
                                    thing=data.thing,
                                    amount=data.amount,
                                    auditorium_id=auditorium_id)


@router.delete('/delete')
async def delete_equipment(id: int) -> None:
    await EquipmentDAO.delete_by_filter(id=id)
