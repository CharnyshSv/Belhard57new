from typing import Optional

from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
#from sqlalchemy.orm import session

from models import create_async_session, Category, Article, User
from schemas import UserInDBSchema, UserSchema

class CRUDUser(object):

    @staticmethod
    @create_async_session
    async def add(user: UserSchema, session: AsyncSession = None) -> Optional[UserInDBSchema]:
        user = User(**user.dict())
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(user)
            return UserInDBSchema(**user.__dict__)

    @staticmethod
    @create_async_session
    async def get(user_id: int, session: AsyncSession = None) -> Optional[UserInDBSchema]:
        user = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = user.first()
        if user:
            return UserInDBSchema(**user[0].__dict__)

    @staticmethod
    @create_async_session
    async def delete(user_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(User)
            .where(User.id == user_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
        user_id: int,
        user: UserInDBSchema,
        session: AsyncSession = None,
        ) -> bool:
            await session.execute(
                update(User)
                .where(User.id == user_id)
                .values(**user.dict())
            )
            try:
                await session.commit()
            except IntegrityError:
                return False
            else:
                return True

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[UserInDBSchema]:
        users = await session.execute(
            select(User)
        )
#       return users.all()
#       return [user[0] for user in users]
            return [UserInDBSchema(**user[0].__dict__) for user in users]