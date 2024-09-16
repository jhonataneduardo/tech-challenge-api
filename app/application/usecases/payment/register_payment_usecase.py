from datetime import datetime

from app.application.gateways.data.payment_data_provider import PaymentDataProviderInterface
from app.application.gateways.data.payment_type_data_provider import PaymentTypeDataProviderInterface
from app.application.gateways.data.order_data_provider import OrderDataProviderInterface

from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.payment_entity import PaymentEntity, PaymentStatus
from app.domain.entities.order_entity import OrderStatus
from app.domain.exceptions import EntityNotFoundException


class RegisterPaymentUseCase(BaseUseCase):

    def __init__(self,
                 payment_data_provider: PaymentDataProviderInterface,
                 payment_type_data_provider: PaymentTypeDataProviderInterface,
                 order_data_provider: OrderDataProviderInterface
                 ) -> None:
        self._payment_data_provider = payment_data_provider
        self._payment_type_data_provider = payment_type_data_provider
        self._order_data_provider = order_data_provider

    def execute(self, **input_data) -> PaymentEntity:
        order_id = input_data.get("order_id")
        type_id = input_data.get("type_id")

        order = self._order_data_provider.get_by_id(order_id=order_id)
        if not order:
            raise EntityNotFoundException("Order not found.")

        payment_type = self._payment_type_data_provider.get_by_id(payment_type_id=type_id)
        if not payment_type:
            raise EntityNotFoundException("Payment type not found.")

        payment = PaymentEntity(
            order=order,
            amount=sum(order.price for order in order.items),
            type=payment_type,
            status=PaymentStatus.APPROVED
        )
        updated_order = self._order_data_provider.patch(
            order_id=payment.order.id,
            status=OrderStatus.RECEIVED.value,
            updated_at=datetime.now()
        )
        payment.order = updated_order

        return self._payment_data_provider.create(payment_entity=payment)
