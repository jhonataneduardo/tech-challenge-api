from typing import List
from app.infrastructure.orm.models import PaymentTypeModel

from app.domain.entities.payment_entity import PaymentTypeEntity
from app.application.gateways.data.payment_type_data_provider import PaymentTypeDataProviderInterface


class PaymentTypeRepository(PaymentTypeDataProviderInterface):

    def create(self, payment_type_entity: PaymentTypeEntity) -> PaymentTypeEntity:
        category = PaymentTypeModel.create(
            name=payment_type_entity.name,
            description=payment_type_entity.description,
            created_at=payment_type_entity.created_at
        )
        return PaymentTypeEntity.from_dict(data=category.model_to_dict())

    def list(self) -> List[PaymentTypeEntity] | None:
        payment_types = PaymentTypeModel.select()
        if not payment_types:
            return None
        return [PaymentTypeEntity.from_dict(data=payment_type.model_to_dict()) for payment_type in payment_types]

    def get_by_id(self, payment_type_id: int) -> PaymentTypeEntity | None:
        payment = PaymentTypeModel.get_or_none(id=payment_type_id)
        if not payment:
            return None
        return PaymentTypeEntity.from_dict(payment.model_to_dict())
