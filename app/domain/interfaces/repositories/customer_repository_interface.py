from typing import Optional, Dict
from abc import ABC, abstractmethod

from app.domain.entities.customer_entity import CustomerEntity


class CustomerRepositoryInterface(ABC):

    @abstractmethod
    def create(self, customer_entity: CustomerEntity) -> Optional[CustomerEntity]:
        raise NotImplementedError

    @abstractmethod
    def find_customer_by_cpf(self, cpf: str) -> Optional[Dict]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, customer_id: int) -> CustomerEntity | None:
        raise NotImplementedError
