from datetime import time, datetime
from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    category_id: int = Field(ge=1, default=None)
    title = str: Field(max_length=24)
    body = str: Field(max_length=1024)
    date_created = time: Field(default = datetime.utcnow())
    author_id = int = Field(ge=1, default=None)


class ArticleInDBSchema(ArticleSchema):
    id: int = Field(ge=1)