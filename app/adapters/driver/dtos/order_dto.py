from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

from app.domain.entities.order_entity import OrderEntity, OrderStatus, OrderItemEntity


class OrderItemDTO(BaseModel):
    id: int
    product_id: int
    quantity: float

    @classmethod
    def from_domain(cls, order_item: OrderItemEntity):
        return cls(id=order_item.id, product_id=order_item.product.id, quantity=order_item.quantity)


class OutputOrderDTO(BaseModel):
    id: int
    customer_id: int
    status: str
    total: float
    items: List[OrderItemDTO]
    created_at: str
    updated_at: Optional[str] = None

    @classmethod
    def from_domain(cls, order: OrderEntity):
        return cls(
            id=order.id,
            customer_id=order.customer.id,
            status=OrderStatus.from_value(order.status).name,
            total=order.total,
            items=[OrderItemDTO.from_domain(order) for order in order.items],
            created_at=order.created_at.strftime(format="%Y-%m-%dT%H:%M:%SZ"),
            updated_at=order.updated_at.strftime(format="%Y-%m-%dT%H:%M:%SZ") if order.updated_at else None
        )

    def to_dict(self):
        return self.model_dump(exclude_none=True)
