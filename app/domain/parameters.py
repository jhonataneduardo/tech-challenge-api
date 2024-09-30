from typing import List, Dict, Optional
from dataclasses import dataclass, asdict, field

from app.domain.entities.order_entity import OrderStatus


@dataclass(frozen=True)
class OrderFilters:
    customer_id: Optional[int] = None
    order: Optional[str] = None
    sort: Optional[str] = None
    status: List[str] = None

    def __post_init__(self):
        object.__setattr__(self, 'order', self.order or "asc")
        object.__setattr__(self, 'sort', self.sort or "created_at")
        object.__setattr__(self, 'status', self.status or [OrderStatus.RECEIVED.name,
                                                           OrderStatus.IN_PREPARATION.name,
                                                           OrderStatus.READY.name])
