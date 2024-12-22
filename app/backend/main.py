import asyncio
import logging
import uvicorn

from core.server import app
from core.bot import bot, dp


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
