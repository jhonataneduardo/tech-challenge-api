from typing import List, Dict

from app.application.gateways.data.order_data_provider import OrderDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.order_entity import OrderEntity
from app.domain.parameters import OrderFilters
from app.domain.exceptions import EntityNotFoundException


class FindAllOrderUseCase(BaseUseCase):

    def __init__(self, order_data_provider: OrderDataProviderInterface):
        self._order_data_provider = order_data_provider

    def execute(self, filters: OrderFilters) -> List[OrderEntity]:
        orders = self._order_data_provider.list(filters=filters)
        if not orders:
            raise EntityNotFoundException("No orders found.")
        return orders
