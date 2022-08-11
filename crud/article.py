from typing import Optional

from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Category, Article, User
from schemas import ArticleInDBSchema, ArticleSchema

class CRUDArticle(object):

    @staticmethod
    @create_async_session
    async def add(article: ArticleSchema, session: AsyncSession = None) -> Optional[ArticleInDBSchema]:
        article = Article(**article.dict())
        session.add(article)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article)
            return ArticleInDBSchema(**article.__dict__)

    @staticmethod
    @create_async_session
    async def get(article_id: int, session: AsyncSession = None) -> Optional[ArticleInDBSchema]:
        article = await session.execute(
          select(Article).where(Article.id == article_id)
        )
        article = article.first()
        if article:
            return ArticleInDBSchema(**article[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[ArticleInDBSchema]:
        articles = await session.execute(
            select(Article)
        )
        return [ArticleInDBSchema(**article[0].__dict__) for article in articles]

    @staticmethod
    @create_async_session
    async def delete(article_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(Article)
            .where(Article.id == article_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            article_id: int,
            article: ArticleInDBSchema,
            session: AsyncSession = None
    ) -> bool:
        await session.execute(
            update(Article)
            .where(Article.id == article_id)
            .values(**article.dict())
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True
