from fastapi import APIRouter

from app.modules.catalog.dependencies import ProductServiceDep
from app.modules.catalog.schemas import ProductCreate, ProductRead

router = APIRouter(prefix="/products", tags=["products"])


@router.post(path="", response_model=ProductRead)
async def create_product(
    data: ProductCreate, service: ProductServiceDep
) -> ProductRead:
    return await service.create_product(data)
