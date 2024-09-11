from app.application.gateways.data.customer_data_provider import CustomerDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase
from app.domain.entities.customer_entity import CustomerEntity
from app.domain.value_objects import CPF
from app.domain.exceptions import CustomerNotFoundException


class FindCustomerByCPFUseCase(BaseUseCase):

    def __init__(self, customer_data_provider: CustomerDataProviderInterface):
        self._customer_data_provider = customer_data_provider

    def execute(self, cpf: str) -> CustomerEntity:
        result = self._customer_data_provider.find_customer_by_cpf(cpf=CPF(cpf).value)

        if not result:
            raise CustomerNotFoundException()

        return CustomerEntity.from_dict(result)
