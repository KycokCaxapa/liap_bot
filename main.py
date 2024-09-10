from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from config import settings

import asyncio
import logging

from app.routers.auditorium.router import router as auditorium_router
from app.routers.auth.router import router as auth_router
from app.routers.equipment.router import router as equipment_router


app = FastAPI()
app.include_router(auditorium_router)
app.include_router(equipment_router)


async def main() -> None:
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()
    dp.include_router(auth_router)
    await dp.start_polling(bot)


@app.get('/')
async def home() -> None:
    return None


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
        asyncio.run(home())
    except KeyboardInterrupt:
        print('[EXIT]')
