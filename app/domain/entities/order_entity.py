from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict, field

from app.domain.entities.base import AggregateRoot
from app.domain.entities.customer_entity import CustomerEntity
from app.domain.entities.product_entity import ProductEntity


class OrderStatus(Enum):
    PENDING = 1
    RECEIVED = 2
    IN_PREPARATION = 3
    READY = 4
    COMPLETED = 5

    @classmethod
    def from_value(cls, value):
        return cls(value=value)


@dataclass(slots=True)
class OrderItemEntity(AggregateRoot):
    product: ProductEntity
    price: float
    quantity: int

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        data_copy["product"] = ProductEntity.from_dict(data=data_copy["product"])
        return cls(**data_copy)


@dataclass(slots=True)
class OrderEntity(AggregateRoot):
    customer: CustomerEntity
    items: List[OrderItemEntity]
    total: float
    status: OrderStatus = OrderStatus.PENDING

    def add_item(self, product: ProductEntity, quantity: int):
        order_item = OrderItemEntity(product, quantity)
        self.items.append(order_item)

    def as_dict(self) -> Dict:
        serialized = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        data_copy["status"] = OrderStatus(data["status"])
        data_copy["customer"] = CustomerEntity.from_dict(data=data["customer"])
        data_copy["items"] = [OrderItemEntity.from_dict(item) for item in data["items"]]
        return cls(**data_copy)
