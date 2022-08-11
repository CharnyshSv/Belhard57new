from datetime import time, datetime
from pydantic import BaseModel, Field


class ArticleCommentSchema(BaseModel):
    comment: str = Field(max_length=140)
    date_created: time = Field(default=datetime.utcnow())
    article_id:int = Field(ge=1, default=None)


class ArticleCommentInDBSchema(ArticleCommentSchema):
    id: int = Field(ge=1)