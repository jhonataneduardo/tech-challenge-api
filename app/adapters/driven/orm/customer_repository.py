from typing import Dict, Optional

from app.adapters.driven.orm.models import CustomerModel

from app.domain.entities.customer_entity import CustomerEntity
from app.domain.interfaces.repositories.customer_repository_interface import CustomerRepositoryInterface


class CustomerRepository(CustomerRepositoryInterface):

    def create(self, customer_entity: CustomerEntity) -> CustomerModel:
        customer = CustomerModel(**customer_entity.as_dict())
        customer.save()
        return customer

    def find_customer_by_cpf(self, cpf: str) -> Optional[Dict]:
        customer = CustomerModel.get_or_none(cpf=cpf)
        if not customer:
            return None
        return customer.model_to_dict()

    def get_by_id(self, customer_id: int) -> CustomerEntity | None:
        customer = CustomerModel.get_or_none(id=customer_id)
        if not customer:
            return None
        return CustomerEntity(**customer.model_to_dict())
