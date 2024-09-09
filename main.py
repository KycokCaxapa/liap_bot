from fastapi import FastAPI

import asyncio


app = FastAPI()


@app.get('/')
async def main():
    return None


if __name__ == '__main__':
    asyncio.run(main())
