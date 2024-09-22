from fastapi import APIRouter, Depends, Query

from fastapi_filter import FilterDepends
from sqlalchemy import select, asc, desc
from app.database.database import async_session
from app.database.models import Auditorium
from app.routers.auditorium.filters import Auditoriumfilter

from app.routers.auditorium.schemas import SAuditorium
from app.routers.auditorium.dao import AuditoriumDAO


router = APIRouter(prefix='/auditorium',
                   tags=['Auditoriums'])


@router.post('/create')
async def create_auditorium(data: SAuditorium) -> None:
    await AuditoriumDAO.create(number=data.number)


@router.get('/get')
async def get_auditorium(number: str) -> SAuditorium:
    auditorium = await AuditoriumDAO.get_by_filter(number=number)
    return auditorium


@router.put('/update')
async def update_auditorium(id: int, data: SAuditorium) -> None:
    await AuditoriumDAO.update_by_id(id, number=data.number)


@router.delete('/delete')
async def delete_auditorium(number: str) -> None:
    await AuditoriumDAO.delete_by_filter(number=number)

@router.get('/filter')
async def filter_auditoriums(filters : Auditoriumfilter = FilterDepends(Auditoriumfilter), sort: str = Query("asc", regex= "^(asc|desc)$")):
    async with async_session() as session:
        query = await session.scalars(select(Auditorium).filter(*filters.get_filters()))
        if sort == "asc":
            query = query.order_by(asc(Auditorium.members))
        else:
            query = query.order_by(desc(Auditorium.members)) 
        return query 