from typing import List
from app.infrastructure.orm.models import OrderModel, OrderItemModel

from app.domain.entities.order_entity import OrderEntity, OrderEntityFilter
from app.application.gateways.data.order_data_provider import OrderDataProviderInterface


class OrderRepository(OrderDataProviderInterface):

    def create(self, order_entity: OrderEntity) -> OrderEntity:
        order = OrderModel.create(
            customer=order_entity.customer.id,
            status=order_entity.status.value,
            total=order_entity.total,
            created_at=order_entity.created_at
        )
        for item in order_entity.items:
            order_item = OrderItemModel(product=item.product.id, price=item.price, quantity=item.quantity)
            order_item.order = order
            order_item.save()
        return OrderEntity.from_dict(order.model_to_dict())

    def list(self, filters: OrderEntityFilter) -> List[OrderEntity]:
        if filters.customer_id:
            orders = OrderModel.select().where(OrderModel.customer == filters.customer_id)
        else:
            orders = OrderModel.select()
        return [OrderEntity.from_dict(order.model_to_dict()) for order in orders]
