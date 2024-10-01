from fastapi.middleware.cors import CORSMiddleware
from aiogram import Bot, Dispatcher
from fastapi import FastAPI
# from app.backend.config import settings
from config import settings

import asyncio
import logging
import uvicorn

from routers.auditorium.router import router as auditorium_router
from routers.equipment.router import router as equipment_router
from routers.auth.router import router as auth_router


app = FastAPI()

app.include_router(auditorium_router)
app.include_router(equipment_router)

origins = ['http://localhost:5173']

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
