from typing import List, Optional
from app.adapters.driven.orm.models import CategoryModel

from app.domain.entities.category_entity import CategoryEntity
from app.domain.interfaces.repositories.category_repository_interface import CategoryRepositoryInterface


class CategoryRepository(CategoryRepositoryInterface):

    def create(self, category_entity: CategoryEntity):
        category = CategoryModel(**category_entity.as_dict())
        category.save()

    def list(self) -> List[CategoryEntity]:
        pass

    def get_by_id(self, category_id: int) -> Optional[CategoryEntity]:
        category = CategoryModel.get_or_none(id=category_id)
        if not category:
            return None
        return CategoryEntity.from_dict(category.model_to_dict())
