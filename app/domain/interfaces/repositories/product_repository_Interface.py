from typing import Optional, List, Dict
from abc import ABC, abstractmethod

from app.domain.entities.product_entity import ProductEntity, ProductEntityFilter


class ProductRepositoryInterface(ABC):

    @abstractmethod
    def create(self, product_entity: ProductEntity) -> Optional[ProductEntity]:
        raise NotImplementedError

    @abstractmethod
    def list(self, filters: ProductEntityFilter) -> List[ProductEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[ProductEntity] | None:
        raise NotImplementedError

    @abstractmethod
    def patch(self, product_id: int, fields: Dict) -> Optional[ProductEntity]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, product_id: int) -> None:
        raise NotImplementedError
