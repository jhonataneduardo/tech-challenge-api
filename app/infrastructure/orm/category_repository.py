from typing import List
from app.infrastructure.orm.models import CategoryModel

from app.domain.entities.category_entity import CategoryEntity
from app.application.gateways.data.category_data_provider import CategoryDataProviderInterface


class CategoryRepository(CategoryDataProviderInterface):

    def create(self, category_entity: CategoryEntity) -> CategoryEntity:
        category = CategoryModel.create(name=category_entity.name, created_at=category_entity.created_at)
        return CategoryEntity.from_dict(data=category.model_to_dict())

    def list(self) -> List[CategoryEntity] | None:
        categories = CategoryModel.select()
        if not categories:
            return None
        return [CategoryEntity.from_dict(data=category.model_to_dict()) for category in categories]

    def get_by_id(self, category_id: int) -> CategoryEntity | None:
        category = CategoryModel.get_or_none(id=category_id)
        if not category:
            return None
        return CategoryEntity.from_dict(category.model_to_dict())

    def get_by_name(self, name: str) -> CategoryEntity | None:
        category = CategoryModel.get_or_none(name=name)
        if not category:
            return None
        return CategoryEntity.from_dict(category.model_to_dict())
