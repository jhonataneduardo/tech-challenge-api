from typing import Dict, Optional, List

from app.infrastructure.orm.models import CustomerModel

from app.domain.entities.customer_entity import CustomerEntity
from app.application.gateways.data.customer_data_provider import CustomerDataProviderInterface


class CustomerRepository(CustomerDataProviderInterface):

    def create(self, customer_entity: CustomerEntity) -> CustomerModel:
        customer = CustomerModel(**customer_entity.as_dict())
        customer.save()
        return customer

    def list(self) -> List[CustomerEntity] | None:
        customers = CustomerModel.select()
        if not customers:
            return None
        return [CustomerEntity.from_dict(data=customer.model_to_dict()) for customer in customers]

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
