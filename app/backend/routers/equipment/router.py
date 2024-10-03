from fastapi_filter import FilterDepends
from fastapi import APIRouter
from typing import List, Optional

from routers.equipment.filters import EquipmentFilter
from routers.equipment.schemas import SEquipment
from routers.equipment.dao import EquipmentDAO


router = APIRouter(prefix='/equipment',
                   tags=['Equipment'])


@router.post('/create')
async def create_equipment(data: SEquipment) -> None:
    await EquipmentDAO.create(thing=data.thing,
                              amount=data.amount,
                              auditorium_id=data.auditorium_id)


@router.get('/get_all')
async def get_all_auditoriums() -> Optional[List[SEquipment]]:
    auditorium = await EquipmentDAO.get_all()
    return auditorium


@router.get('/get_by_filters')
async def get_equipment_by_filters(filters: EquipmentFilter = FilterDepends(EquipmentFilter)) -> Optional[List[SEquipment]]:
    equipment = await EquipmentDAO.get_by_filters(filters)
    return equipment


@router.put('/update')
async def update_equipment(id: int, data: SEquipment) -> Optional[List[SEquipment]]:
    await EquipmentDAO.update_by_id(id,
                                    thing=data.thing,
                                    amount=data.amount,
                                    auditorium_id=data.auditorium_id)


@router.delete('/delete')
async def delete_equipment(id: int) -> None:
    await EquipmentDAO.delete_by_filter(id=id)
