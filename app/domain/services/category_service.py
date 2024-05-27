from app.domain.interfaces.repositories.category_repository_interface import CategoryRepositoryInterface
from app.domain.entities.category_entity import CategoryEntity


class CategoryService:

    def __init__(self, category_repository: CategoryRepositoryInterface) -> None:
        self._category_repository = category_repository

    def create_category(self, name: str) -> CategoryEntity:
        category = CategoryEntity(name=name)
        self._category_repository.create(category_entity=category)
        return category
