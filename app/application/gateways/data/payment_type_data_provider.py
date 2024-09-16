from typing import Optional, List
from abc import ABC, abstractmethod

from app.domain.entities.payment_entity import PaymentTypeEntity


class PaymentTypeDataProviderInterface(ABC):

    @abstractmethod
    def create(self, payment_type_entity: PaymentTypeEntity) -> Optional[PaymentTypeEntity]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, payment_type_id: int) -> Optional[PaymentTypeEntity] | None:
        raise NotImplementedError
