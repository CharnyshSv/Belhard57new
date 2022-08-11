from typing import Optional

from sqlalchemy import select, update, delete, or_, and_
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models import create_async_session, Category, Article, User, ArticleComment
from schemas import ArticleCommentInDBSchema, ArticleCommentSchema


class CRUDArticleComment(object):

    @staticmethod
    @create_async_session
    async def add(article_comment: ArticleCommentSchema, session: AsyncSession = None) -> Optional[
        ArticleCommentInDBSchema]:
        article_comment = ArticleComment(**article_comment.dict())
        await session.add(article_comment)
        try:
            await session.commit()
        except IntegrityError:
            pass
        else:
            await session.refresh(article_comment)
            return ArticleCommentInDBSchema(**article_comment.__dict__)

    @staticmethod
    @create_async_session
    async def get(article_comment_id: int, session: AsyncSession = None) -> Optional[ArticleCommentInDBSchema]:
        article_comment = await session.execute(
            select(ArticleComment).where(ArticleComment.id == article_comment_id)
        )
        article_comment = article_comment.first()
        if article_comment:
            return ArticleCommentInDBSchema(**article_comment[0].__dict__)

    @staticmethod
    @create_async_session
    async def get_all(session: AsyncSession = None) -> list[ArticleCommentInDBSchema]:
        articles_comments = await session.execute(
            select(ArticleComment)
        )
        return [ArticleCommentInDBSchema(**article_comment[0].__dict__) for article_comment in articles_comments]

    @staticmethod
    @create_async_session
    async def delete(article_comment_id: int, session: AsyncSession = None) -> None:
        await session.execute(
            delete(ArticleComment)
            .where(ArticleComment.id == article_comment_id)
        )
        await session.commit()

    @staticmethod
    @create_async_session
    async def update(
            article_comment_id: int,
            article: ArticleCommentInDBSchema,
            session: AsyncSession = None
    ) -> bool:
        await session.execute(
            update(ArticleComment)
            .where(ArticleComment.id == article_comment_id)
            .values(**article_comment_id.dict())
        )
        try:
            await session.commit()
        except IntegrityError:
            return False
        else:
            return True
