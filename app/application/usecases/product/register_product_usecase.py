from app.application.gateways.data.product_data_provider import ProductDataProviderInterface
from app.application.gateways.data.category_data_provider import CategoryDataProviderInterface

from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.product_entity import ProductEntity
from app.domain.exceptions import EntityNotFoundException


class RegisterProductUseCase(BaseUseCase):

    def __init__(self,
                 product_data_provider: ProductDataProviderInterface,
                 category_data_provider: CategoryDataProviderInterface
                 ) -> None:
        self._product_data_provider = product_data_provider
        self._category_data_provider = category_data_provider

    def execute(self, **input_data) -> ProductEntity:
        category_id = input_data.get("category_id")
        name = input_data.get("name")
        description = input_data.get("description")
        price = input_data.get("price")

        category = self._category_data_provider.get_by_id(category_id=category_id)
        if not category:
            raise EntityNotFoundException("Category not found.")

        product_entity = ProductEntity(
            name=name,
            description=description,
            price=price,
            category=category
        )

        return self._product_data_provider.create(product_entity=product_entity)
