from aiogram import Bot, Dispatcher

from routers.auth.tgrouter import router as tg_auth_router
from config import settings



bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

dp.include_router(tg_auth_router)
