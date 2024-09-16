from app.application.gateways.data.category_data_provider import CategoryDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.category_entity import CategoryEntity
from app.domain.exceptions import EntityNotFoundException, EntityAlreadyExistsException


class RegisterCategoryUseCase(BaseUseCase):

    def __init__(self, category_data_provider: CategoryDataProviderInterface) -> None:
        self._category_data_provider = category_data_provider

    def execute(self, name: str) -> CategoryEntity:
        if self._category_data_provider.get_by_name(name=name):
            raise EntityAlreadyExistsException("There is already a registered category with this name.")
        category = CategoryEntity(name=name)
        return self._category_data_provider.create(category_entity=category)
