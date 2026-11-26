
from typing import Any
import uuid
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field

from app.modules.catalog.models import Category


class ProductBase(BaseModel):
    name:str = Field(min_length=2,max_length=255)
    brand:str = Field(min_length=2, max_length=255)
    category: Category
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    stock: int = Field(ge=0)
    warranty_months: int = Field(ge=0, default=12)
    description: str = Field(default="")
    specs: dict[str, Any] = Field(default={})

class ProductCreate(ProductBase):
    slug: str = Field(min_length=2, max_length=255)

class ProductRead(ProductBase):
    id: uuid.UUID
    slug: str
    in_stock: bool

    model_config = ConfigDict(from_attributes=True)

class ProductUpdate(BaseModel):
    """Every field is optional, only the provided fields will be updated."""

    name: str | None = Field(default=None, min_length=2, max_length=255)
    price: Decimal | None = Field(default=None, gt=0, max_digits=10, decimal_places=2)
    stock: int | None = Field(default=None, ge=0)
    warranty_months: int | None = Field(default=None, ge=0)
    description: str | None = Field(default=None)
    specs: dict[str, Any] | None = Field(default=None)

class SortOption(str, Enum):
    NEWEST = "newest"
    PRICE_ASC = "price_asc"
    PRICE_DESC = "price_desc"
    NAME = "name"

class ProductFilters(BaseModel):

    q: str | None = Field(default=None, min_length=2, max_length=100)
    category: Category | None = None
    brand: str | None = None
    max_price: Decimal | None = Field(default=None, gt=0)
    min_price: Decimal | None = Field(default=None, gt=0)
    in_stock: bool | None = None
    sort: SortOption = SortOption.NEWEST
    page: int  = Field(default=1, ge=1)
    page_size: int = Field(default=10, ge=1, le=500)

class Page(BaseModel):
    items: list[ProductRead]
    total: int
    page: int
    page_size: int