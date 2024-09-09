from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from config import settings

import asyncio
import logging

from app.routers.auth.router import router as auth_router


app = FastAPI()


async def main() -> None:
    bot = Bot(token=settings.TOKEN)
    dp = Dispatcher()
    dp.include_router(auth_router)
    await dp.start_polling(bot)


@app.get('/')
async def home() -> None:
    return None


if __name__ == '__main__':
    # asyncio.run(main())
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
        asyncio.run(home())
    except KeyboardInterrupt:
        print('[EXIT]')
