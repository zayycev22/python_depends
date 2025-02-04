from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DB_HOST = "DB_HOST"
DB_PORT = "DB_PORT"
DB_USER = "DB_USER"
DB_PASSWORD = "DB_PASSWORD"
DB_NAME = "DB_NAME"

DATABASE_URL = "postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(
    url=DATABASE_URL.format(DB_USER=DB_USER, DB_HOST=DB_HOST, DB_PORT=DB_PORT, DB_PASSWORD=DB_PASSWORD,
                            DB_NAME=DB_NAME))

async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
