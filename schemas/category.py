from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name: str = Field(max_length=24)
    parent_id: int = Field(ge=1, default=None)


class CategoryInDBSchema(CategorySchema):
    id: int = Field(ge=1)