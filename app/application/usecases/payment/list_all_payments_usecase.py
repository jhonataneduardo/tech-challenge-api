from typing import List

from app.application.gateways.data.payment_data_provider import PaymentDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase

from app.domain.entities.payment_entity import PaymentEntity, PaymentEntityFilter
from app.domain.exceptions import EntityNotFoundException


class ListAllPaymentsUseCase(BaseUseCase):

    def __init__(self, payment_data_provider: PaymentDataProviderInterface):
        self._payment_data_provider = payment_data_provider

    def execute(self, **filters) -> List[PaymentEntity]:
        payment_filters = PaymentEntityFilter(order_id=filters.get("order_id"), status=filters.get("status"))

        payments = self._payment_data_provider.list(filters=payment_filters)
        if not payments:
            raise EntityNotFoundException("No payments found.")

        return payments
