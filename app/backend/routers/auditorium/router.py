from fastapi_filter import FilterDepends
from typing import List, Optional
from fastapi import APIRouter

from routers.auditorium.filters import AuditoriumFilter
from routers.auditorium.schemas import SAuditorium
from routers.auditorium.dao import AuditoriumDAO


router = APIRouter(prefix='/auditorium',
                   tags=['Auditoriums'])


@router.post('/create')
async def create_auditorium(data: SAuditorium) -> None:
    await AuditoriumDAO.create(number=data.number,
                               members=data.members,
                               projector=data.projector)


@router.get('/get_all')
async def get_all_auditoriums() -> Optional[List[SAuditorium]]:
    auditorium = await AuditoriumDAO.get_all()
    return auditorium


@router.get('/get_by_filters')
async def get_auditoriums_by_filters(filters: AuditoriumFilter = FilterDepends(AuditoriumFilter)) -> Optional[List[SAuditorium]]:
    auditorium = await AuditoriumDAO.get_by_filters(filters)
    return auditorium


@router.put('/update')
async def update_auditorium(id: int, data: SAuditorium) -> SAuditorium:
    await AuditoriumDAO.update_by_id(id,
                                     number=data.number,
                                     members=data.members,
                                     projector=data.projector)
    return SAuditorium


@router.delete('/delete')
async def delete_auditorium(number: str) -> None:
    await AuditoriumDAO.delete_by_filter(number=number)
