from typing import Optional

from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Category, Article
from schemas import CategoryInDBSchema, CategorySchema

class CRUDCategory(object):

    @staticmethod
    @create_async_session
    async def add(category: CategorySchema, session: AsyncSession = None) -> Optional[CategoryInDBSchema]:
        category = Category(**category.dict())
        session.add(category)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(category)
            return CategoryInDBSchema(**category.__dict__)

    @staticmethod
    @create_async_session
    async def get(category_id: int, session: AsyncSession = None) -> Optional[CategoryInDBSchema]:
        category = await session.execute(
          select(Category).where(Category.id == category_id)
        )
        category = category.first()
        if category:
            return CategoryInDBSchema(**category[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(parent_id: int = None, session: AsyncSession = None) -> list[CategoryInDBSchema]:
        if parent_id:
            categories = await session.execute(
                select(Category)
                .where(Category.parent_id == parent_id)
                .order_by(Category.id)
            )
        else:
            categories = await session.execute(
                select(Category)
            )
        return [CategoryInDBSchema(**category[0].__dict__) for category in categories]

    @staticmethod
    @create_async_session
    async def delete(category_id: int, session: AsyncSession = None) -> None:
        categories = await session.execute(
            delete(Category)
                .where(Category.id == category_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            category: CategoryInDBSchema,
            session: AsyncSession = None
    ) -> bool:
        await session.execute(
            update(Category)
            .where(Category.id == category.id)
            .values(**category.dict())
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True

    @staticmethod
    @create_async_session
    async def get_articles(category_id: int, session: AsyncSession = None) -> list[tuple[Category,Article]]:
        response = await session.execute(
            select(Category, Article)
            .join(Article. Category.id == Article.category_id)
            .where(Category.id == category_id)
        )
        return response.all()