from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router

from routers.auth.dao import UserDAO
from routers.auth.keyboards import keyboard


router = Router()


@router.message(CommandStart())
async def start(message: Message) -> None:
    tg_id = message.from_user.id
    username = message.from_user.full_name
    if await UserDAO.user_exists(tg_id):
        await message.answer('Снова привет!',
                             reply_markup=keyboard())
    else:
        await UserDAO.create(tg_id=tg_id, username=username, role='student')
        await message.answer('Привет!',
                             reply_markup=keyboard())
