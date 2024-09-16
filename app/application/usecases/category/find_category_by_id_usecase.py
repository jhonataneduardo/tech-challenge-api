from app.application.gateways.data.category_data_provider import CategoryDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.category_entity import CategoryEntity
from app.domain.exceptions import EntityNotFoundException


class FindCategoryByIdUseCase(BaseUseCase):

    def __init__(self, category_data_provider: CategoryDataProviderInterface) -> None:
        self._category_data_provider = category_data_provider

    def execute(self, category_id: int) -> CategoryEntity:
        category = self._category_data_provider.get_by_id(category_id=category_id)
        if not category:
            raise EntityNotFoundException("Category not found.")
        return category
