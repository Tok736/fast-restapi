import asyncio

from models import Base
from database import engine


async def database_init() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        
asyncio.run(database_init())