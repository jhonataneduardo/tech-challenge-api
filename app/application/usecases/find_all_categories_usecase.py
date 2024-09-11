from typing import List

from app.application.gateways.data.category_data_provider import CategoryDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.category_entity import CategoryEntity
from app.domain.exceptions import EntityNotFoundException


class FindAllCategoriesUseCase(BaseUseCase):

    def __init__(self, category_data_provider: CategoryDataProviderInterface) -> None:
        self._category_data_provider = category_data_provider

    def execute(self) -> List[CategoryEntity]:
        categories = self._category_data_provider.list()
        if not categories:
            raise EntityNotFoundException("There are no registered categories.")
        return categories
