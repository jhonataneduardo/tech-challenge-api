from typing import List, Dict

from app.application.gateways.data.order_data_provider import OrderDataProviderInterface
from app.application.gateways.data.product_data_provider import ProductDataProviderInterface
from app.application.gateways.data.customer_data_provider import CustomerDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.order_entity import OrderEntity, OrderItemEntity
from app.domain.exceptions import EntityNotFoundException


class RegisterOrderUseCase(BaseUseCase):

    def __init__(self,
                 order_data_provider: OrderDataProviderInterface,
                 product_data_provider: ProductDataProviderInterface,
                 customer_data_provider: CustomerDataProviderInterface
                 ):
        self._order_data_provider = order_data_provider
        self._product_data_provider = product_data_provider
        self._customer_data_provider = customer_data_provider

    def _prepare_order_item(self, item: Dict) -> OrderItemEntity:
        product = self._product_data_provider.get_by_id(product_id=item.get("product_id"))
        if not product:
            raise EntityNotFoundException(f"Product {item.get('product_id')} not found.")
        return OrderItemEntity(product=product, price=item.get("price"), quantity=item.get("quantity"))

    def execute(self, customer_id: int, items: Dict, total: float) -> OrderEntity:
        customer = self._customer_data_provider.get_by_id(customer_id=customer_id)
        if not customer:
            raise EntityNotFoundException("Customer not found.")
        items = [self._prepare_order_item(item) for item in items]
        order = OrderEntity(customer=customer, items=items, total=total)
        return self._order_data_provider.create(order_entity=order)
