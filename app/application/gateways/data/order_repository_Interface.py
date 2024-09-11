from typing import Optional, List
from abc import ABC, abstractmethod

from app.domain.entities.order_entity import OrderEntity, OrderEntityFilter


class OrderRepositoryInterface(ABC):

    @abstractmethod
    def create(self, order_entity: OrderEntity) -> Optional[OrderEntity]:
        raise NotImplementedError

    @abstractmethod
    def list(self, filters: OrderEntityFilter) -> List[OrderEntity]:
        raise NotImplementedError
