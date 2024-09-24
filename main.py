from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher
from fastapi import FastAPI
from config import settings

import threading
import asyncio
import logging
import uvicorn

from app.backend.routers.auditorium.router import router as auditorium_router
from app.backend.routers.auth.router import router as auth_router
from app.backend.routers.equipment.router import router as equipment_router


app = FastAPI()

app.include_router(auditorium_router)
app.include_router(equipment_router)

origins = ['http://localhost:3000']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=['POST', 'GET', 'PUT', 'DELETE'],
                   allow_headers=['*']) #Возможно, заголовки также придётся прописать вручную, например, 'Content-Type', 'Set-Cookie'

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()
dp.include_router(auth_router)


async def start_bot() -> None:
    await dp.start_polling(bot)


async def start_server() -> None:
    config = uvicorn.Config(app,
                            host='localhost',
                            port=8000)
    server = uvicorn.Server(config)
    await server.serve()


async def main() -> None:
    await asyncio.gather(start_bot(), start_server())


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('[EXIT]')
