from sqlmodel import SQLModel, Field
from typing import Optional


class Brand(SQLModel, table=True):
    id: int = Field(primary_key=True, index=True)
    name: str = Field(max_length=255)
    description: str = Field(max_length=500)
    image_url: str = Field(max_length=255)


class BrandUpdate(SQLModel):
    name: str = None
    description: str = None
    image_url: str = None
