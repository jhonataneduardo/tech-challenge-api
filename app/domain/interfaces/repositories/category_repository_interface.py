from typing import List, Optional
from abc import ABC, abstractmethod

from app.domain.entities.category_entity import CategoryEntity


class CategoryRepositoryInterface(ABC):

    @abstractmethod
    def create(self, category_entity: CategoryEntity) -> None:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[CategoryEntity]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        raise NotImplementedError
