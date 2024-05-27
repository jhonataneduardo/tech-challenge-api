from typing import Optional
from pydantic import BaseModel

from app.domain.entities.product_entity import ProductEntity


class OutputProductDTO(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int
    created_at: str
    updated_at: Optional[str] = None

    @classmethod
    def from_domain(cls, product: ProductEntity):
        return cls(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category.id,
            created_at=product.created_at.strftime(format="%Y-%m-%dT%H:%M:%SZ"),
            updated_at=product.updated_at.strftime(format="%Y-%m-%dT%H:%M:%SZ") if product.updated_at else None
        )

    def to_dict(self):
        return self.model_dump(exclude_none=True)
