from typing import List, Dict

from app.application.gateways.data.order_repository_Interface import OrderRepositoryInterface
from app.application.gateways.data.product_repository_Interface import ProductRepositoryInterface
from app.application.gateways.data.customer_data_provider import CustomerRepositoryInterface

from app.domain.entities.order_entity import OrderEntity, OrderItemEntity, OrderEntityFilter
from app.domain.exceptions import EntityNotFoundException


class OrderService:

    def __init__(self,
                 order_repository: OrderRepositoryInterface,
                 product_repository: ProductRepositoryInterface,
                 customer_repository: CustomerRepositoryInterface
                 ) -> None:
        self._order_repository = order_repository
        self._product_repository = product_repository
        self._customer_repository = customer_repository

    def _prepare_order_item(self, item: Dict) -> OrderItemEntity:
        product = self._product_repository.get_by_id(product_id=item.get("product_id"))
        if not product:
            raise EntityNotFoundException(f"Product {item.get('product_id')} not found.")
        return OrderItemEntity(product=product, price=item.get("price"), quantity=item.get("quantity"))

    def create_order(self,
                     customer_id: int,
                     items: Dict,
                     total: float
                     ) -> OrderEntity:
        customer = self._customer_repository.get_by_id(customer_id=customer_id)
        if not customer:
            raise EntityNotFoundException("Customer not found.")
        items = [self._prepare_order_item(item) for item in items]
        order = OrderEntity(customer=customer, items=items, total=total)
        return self._order_repository.create(order_entity=order)

    def all_orders(self, **filters) -> List[OrderEntity]:
        order_filters = OrderEntityFilter(customer_id=filters.get("customer_id"))
        orders = self._order_repository.list(filters=order_filters)
        if not orders:
            raise EntityNotFoundException("No orders found.")
        return orders
