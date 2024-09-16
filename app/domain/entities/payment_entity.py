from enum import Enum
from typing import Dict, Optional
from dataclasses import dataclass, asdict

from app.domain.entities.base import AggregateRoot
from app.domain.entities.order_entity import OrderEntity


class PaymentStatus(Enum):
    APPROVED = 1
    REFUSED = 2
    ERROR = 3

    @classmethod
    def from_value(cls, value):
        return cls(value=value)


@dataclass(slots=True)
class PaymentTypeEntity(AggregateRoot):
    name: str
    description: str

    @classmethod
    def from_dict(cls, data: Dict):
        return cls(**data)


@dataclass(slots=True)
class PaymentEntity(AggregateRoot):
    order: OrderEntity
    amount: float
    type: PaymentTypeEntity
    status: PaymentStatus

    def as_dict(self) -> Dict:
        serialized = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        data_copy["order"] = OrderEntity.from_dict(data=data["order"])
        data_copy["type"] = PaymentTypeEntity.from_dict(data=data["type"])
        data_copy["status"] = PaymentStatus(data["status"])
        return cls(**data_copy)


@dataclass(frozen=True)
class PaymentEntityFilter:
    order_id: Optional[int] = None
    status: Optional[str] = PaymentStatus.APPROVED.name
