from typing import Optional, List, Dict
from abc import ABC, abstractmethod

from app.domain.entities.order_entity import OrderEntity
from app.domain.parameters import OrderFilters


class OrderDataProviderInterface(ABC):

    @abstractmethod
    def create(self, order_entity: OrderEntity) -> Optional[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def list(self, filters: OrderFilters) -> List[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[OrderEntity] | None:
        raise NotImplementedError

    @abstractmethod
    def patch(self, order_id: int, **fields) -> Optional[OrderEntity]:
        raise NotImplementedError
