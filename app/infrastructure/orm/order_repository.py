from typing import List, Optional
from peewee import SQL

from app.infrastructure.orm.models import OrderModel, OrderItemModel

from app.domain.entities.order_entity import OrderEntity, OrderStatus
from app.domain.parameters import OrderFilters

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

    def list(self, filters: OrderFilters) -> List[OrderEntity]:
        where = (OrderModel.status.in_([OrderStatus[status].value for status in filters.status]),)

        if filters.customer_id:
            where += (OrderModel.customer == filters.customer_id,)

        orders = (OrderModel.select()
                  .where(*where)
                  .order_by(SQL(f"{filters.sort} {filters.order}, id {filters.order}")))

        return [OrderEntity.from_dict(order.model_to_dict()) for order in orders]

    def get_by_id(self, order_id: int) -> Optional[OrderEntity] | None:
        order = OrderModel.get_or_none(id=order_id)
        if not order:
            return None
        return OrderEntity.from_dict(order.model_to_dict())

    def patch(self, order_id: int, **fields) -> Optional[OrderEntity] | None:
        order = OrderModel.get_or_none(id=order_id)
        if not order:
            return None
        for key, value in fields.items():
            if hasattr(OrderEntity, key):
                setattr(order, key, value)
        updated_order = OrderEntity.from_dict(order.model_to_dict())
        order.save()
        return updated_order
