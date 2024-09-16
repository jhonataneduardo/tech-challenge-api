from datetime import datetime

from app.application.gateways.data.payment_data_provider import PaymentDataProviderInterface
from app.application.gateways.data.order_data_provider import OrderDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.payment_entity import PaymentEntity
from app.domain.entities.order_entity import OrderStatus
from app.domain.exceptions import EntityNotFoundException


class UpdateStatusPaymentUseCase(BaseUseCase):

    def __init__(self,
                 payment_data_provider: PaymentDataProviderInterface,
                 order_data_provider: OrderDataProviderInterface
                 ):
        self._payment_data_provider = payment_data_provider
        self._order_data_provider = order_data_provider

    def execute(self, payment_id: int, status: str) -> PaymentEntity:
        payment = self._payment_data_provider.get_by_id(payment_id=payment_id)

        if not payment:
            raise EntityNotFoundException("No payments found.")

        updated_payment = self._payment_data_provider.patch(payment_id=payment_id, status=status)
        updated_order = self._order_data_provider.patch(
            order_id=payment.order.id,
            status=OrderStatus.RECEIVED.value,
            updated_at=datetime.now()
        )
        updated_payment.order = updated_order

        return updated_payment
