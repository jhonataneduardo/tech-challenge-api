from typing import Optional
from pydantic import BaseModel

from app.domain.entities.customer_entity import CustomerEntity


class OutputCustomerDTO(BaseModel):
    id: int
    name: str
    email: str
    cpf: str
    created_at: str
    updated_at: Optional[str] = None

    @classmethod
    def from_domain(cls, customer: CustomerEntity):
        return cls(
            id=customer.id,
            name=customer.name,
            email=customer.email.value,
            cpf=customer.cpf.value,
            created_at=customer.created_at.strftime(format="%Y-%m-%dT%H:%M:%SZ"),
            updated_at=customer.updated_at.strftime(format="%Y-%m-%dT%H:%M:%SZ") if customer.updated_at else None
        )

    def to_dict(self):
        return self.model_dump(exclude_none=True)
