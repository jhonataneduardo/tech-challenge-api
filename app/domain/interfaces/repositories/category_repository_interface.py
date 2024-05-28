from typing import List, Optional
from abc import ABC, abstractmethod

from app.domain.entities.category_entity import CategoryEntity


class CategoryRepositoryInterface(ABC):

    @abstractmethod
    def create(self, category_entity: CategoryEntity) -> CategoryEntity:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[CategoryEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, category_id: int) -> CategoryEntity:
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, name: str) -> CategoryEntity:
        raise NotImplementedError
