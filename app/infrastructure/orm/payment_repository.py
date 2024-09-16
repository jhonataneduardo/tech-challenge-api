from typing import List, Optional
from app.infrastructure.orm.models import PaymentModel

from app.domain.entities.payment_entity import PaymentEntity, PaymentEntityFilter, PaymentStatus
from app.application.gateways.data.payment_data_provider import PaymentDataProviderInterface


class PaymentRepository(PaymentDataProviderInterface):

    def create(self, payment_entity: PaymentEntity) -> PaymentEntity:
        payment = PaymentModel.create(
            order_id=payment_entity.order.id,
            type_id=payment_entity.type.id,
            amount=payment_entity.amount,
            status=payment_entity.status.value,
            created_at=payment_entity.created_at
        )
        return PaymentEntity.from_dict(data=payment.model_to_dict())

    def list(self, filters: PaymentEntityFilter) -> List[PaymentEntity]:
        where = tuple()
        if filters.order_id:
            where += (PaymentModel.order == filters.order_id,)
        if filters.status:
            where += (PaymentModel.status == PaymentStatus[filters.status].value,)
        orders = PaymentModel.select().where(*where) if len(where) > 0 else PaymentModel.select()
        return [PaymentEntity.from_dict(order.model_to_dict()) for order in orders]

    def get_by_id(self, payment_id: int) -> Optional[PaymentEntity] | None:
        payment = PaymentModel.get_or_none(id=payment_id)
        if not payment:
            return None
        return PaymentEntity.from_dict(payment.model_to_dict())

    def patch(self, payment_id: int, **fields) -> Optional[PaymentEntity] | None:
        payment = PaymentModel.get_or_none(id=payment_id)
        if not payment:
            return None
        for key, value in fields.items():
            if hasattr(PaymentEntity, key):
                setattr(payment, key, value)
        updated_payment = PaymentEntity.from_dict(payment.model_to_dict())
        payment.save()
        return updated_payment
