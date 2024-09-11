from typing import List

from app.application.gateways.data.category_repository_interface import CategoryRepositoryInterface
from app.domain.entities.category_entity import CategoryEntity
from app.domain.exceptions import EntityNotFoundException, EntityAlreadyExistsException


class CategoryService:

    def __init__(self, category_repository: CategoryRepositoryInterface) -> None:
        self._category_repository = category_repository

    def create_category(self, name: str) -> CategoryEntity:
        if self._category_repository.get_by_name(name=name):
            raise EntityAlreadyExistsException("There is already a registered category with this name.")
        category = CategoryEntity(name=name)
        return self._category_repository.create(category_entity=category)

    def all_categories(self) -> List[CategoryEntity]:
        categories = self._category_repository.list()
        if not categories:
            raise EntityNotFoundException("There are no registered categories.")
        return categories

    def get_category_by_id(self, category_id: int) -> CategoryEntity:
        category = self._category_repository.get_by_id(category_id=category_id)
        if not category:
            raise EntityNotFoundException("Category not found.")
        return category

    def get_category_by_name(self, name: str) -> CategoryEntity:
        category = self._category_repository.get_by_name(name=name)
        if not category:
            raise EntityNotFoundException("Category not found.")
        return category
