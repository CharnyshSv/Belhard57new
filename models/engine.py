from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL: str = "postgresql://svetlgo:belhard@localhost:5432/bh57"
DATABASE_ASYNC_URL: str = "postgresql+asyncpg://svetlgo:belhard@localhost:5432/bh57"
engine = create_engine(DATABASE_URL)
async_engine = create_async_engine(DATABASE_ASYNC_URL)
Session = sessionmaker(bind=engine)

def create_session(func):
    def wrapper(**kwargs):
        with Session() as session:
            return func(**kwargs, session=session)
    return wrapper


def create_async_session(func):
    async def wrapper(**kwargs):
        async with AsyncSession(bind=async_engine) as session:
            return await func(**kwargs, session=session)
    return wrapper