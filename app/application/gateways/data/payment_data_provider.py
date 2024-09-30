from typing import Optional, List, Dict
from abc import ABC, abstractmethod

from app.domain.entities.payment_entity import PaymentEntity, PaymentEntityFilter


class PaymentDataProviderInterface(ABC):

    @abstractmethod
    def create(self, payment_entity: PaymentEntity) -> Optional[PaymentEntity]:
        raise NotImplementedError

    @abstractmethod
    def list(self, filters: PaymentEntityFilter) -> List[PaymentEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, payment_id: int) -> Optional[PaymentEntity] | None:
        raise NotImplementedError

    @abstractmethod
    def patch(self, payment_id: int, **fields) -> Optional[PaymentEntity]:
        raise NotImplementedError
