from typing import List

from app.application.gateways.data.product_data_provider import ProductDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.product_entity import ProductEntity, ProductEntityFilter
from app.domain.exceptions import EntityNotFoundException


class ListAllProductsUseCase(BaseUseCase):

    def __init__(self, product_data_provider: ProductDataProviderInterface) -> None:
        self._product_data_provider = product_data_provider

    def execute(self, **filters) -> List[ProductEntity]:
        product_filters = ProductEntityFilter(category_id=filters.get("category_id"))

        products = self._product_data_provider.list(filters=product_filters)

        if not products:
            raise EntityNotFoundException("No products found.")

        return products
