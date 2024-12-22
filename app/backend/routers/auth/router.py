from typing import List, Optional
from fastapi import APIRouter

from routers.auth.schema import SUser
from routers.auth.dao import UserDAO


router = APIRouter(prefix='/users',
                   tags=['Users'])


@router.get('/get_all')
async def get_all_users() -> Optional[List[SUser]]:
    '''Only for debugging.'''
    users = await UserDAO.get_all()
    return users


@router.get('/get_role')
async def get_user_role(tg_id: int) -> str:
    role = await UserDAO.get_user_role(tg_id)
    return role
