from fastapi import APIRouter
from typing import List

from routers.equipment.schemas import SEquipment
from routers.equipment.dao import EquipmentDAO


router = APIRouter(prefix='/equipment',
                   tags=['Equipment'])


@router.post('/create')
async def create_equipment(data: SEquipment) -> None:
    await EquipmentDAO.create(thing=data.thing,
                              auditorium_id=data.auditorium_id)


@router.get('/get_all')
async def get_all_auditoriums() -> List[SEquipment]:
    auditorium = await EquipmentDAO.get_all()
    return auditorium


@router.get('/get')
async def get_equipment(id: int) -> SEquipment:
    equipment = await EquipmentDAO.get_by_filter(id=id)
    return equipment


@router.put('/update')
async def update_equipment(id: int, data: SEquipment) -> None:
    await EquipmentDAO.update_by_id(id,
                                    thing=data.thing,
                                    auditorium_id=data.auditorium_id)


@router.delete('/delete')
async def delete_equipment(id: int) -> None:
    await EquipmentDAO.delete_by_filter(id=id)
