from typing import Dict
from datetime import datetime

from app.application.gateways.data.product_data_provider import ProductDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.product_entity import ProductEntity
from app.domain.exceptions import EntityNotFoundException


class UpdateProductUseCase(BaseUseCase):

    def __init__(self, product_data_provider: ProductDataProviderInterface) -> None:
        self._product_data_provider = product_data_provider

    def execute(self, product_id: int, fields: Dict) -> ProductEntity:
        fields["updated_at"] = datetime.now()

        product = self._product_data_provider.patch(product_id=product_id, fields=fields)
        if not product:
            raise EntityNotFoundException("Product not found.")
        
        return product
