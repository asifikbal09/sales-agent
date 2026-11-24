
from sqlalchemy.ext.asyncio import AsyncSession

from app.modules.catalog.models import Product


class ProductRepository:
    def __init__(self, session: AsyncSession)-> None:
        self.db_session: AsyncSession = session

    async def add(self, product: Product)-> Product:
        self.db_session.add(instance=product)
        return await self.save(product)

    async def save(self, product: Product)-> Product:
        await self.db_session.flush()
        await self.db_session.refresh(instance=product)
        return product

