import enum
import uuid
from decimal import Decimal
from typing import Any

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Enum,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, TimestampMixin


class Category(str, enum.Enum):
    PHONE = "phone"
    LAPTOP = "laptop"
    WATCH = "watch"
    TABLET = "tablet"
    MONITOR = "monitor"
    ACCESSORY = "accessory"


class Product(Base, TimestampMixin):
    __tablename__ = "products"
    __table_args__ = (
        CheckConstraint(sqltext="price > 0", name="price_positive"),
        CheckConstraint(sqltext="stock >= 0", name="stock_non_negative"),
    )

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(length=255), nullable=False)
    slug: Mapped[str] = mapped_column(String(length=255), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    price: Mapped[Decimal] = mapped_column(
        Numeric(precision=10, scale=2), nullable=False
    )
    brand: Mapped[str] = mapped_column(String(length=255), nullable=False, index=True)
    stock: Mapped[int] = mapped_column(Integer, default=0, server_default="0")
    specs: Mapped[dict[str, Any]] = mapped_column(
        JSONB, default=dict, server_default="{}"
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true"
    )
    warranty_months: Mapped[int] = mapped_column(
        Integer, default=12, server_default="12"
    )
    category: Mapped[Category] = mapped_column(
        Enum(
            Category,
            native_enum=False,
            length=20,
            value_callable=lambda e: [m.value for m in e],
        ),
        index=True,
    )

    @property
    def in_stock(self) -> bool:
        return self.stock > 0
