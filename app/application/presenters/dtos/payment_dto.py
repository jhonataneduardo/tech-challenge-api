from pydantic import BaseModel

from app.domain.entities.payment_entity import PaymentEntity, PaymentStatus


class OutputPaymentDTO(BaseModel):
    id: int
    order_id: int
    amount: float
    type_id: int
    status: str
    created_at: str

    @classmethod
    def from_domain(cls, payment: PaymentEntity):
        return cls(
            id=payment.id,
            order_id=payment.order.id,
            amount=payment.amount,
            type_id=payment.type.id,
            status=payment.status.name,
            created_at=payment.created_at.strftime(format="%Y-%m-%dT%H:%M:%SZ")
        )

    def to_dict(self):
        return self.model_dump(exclude_none=True)
