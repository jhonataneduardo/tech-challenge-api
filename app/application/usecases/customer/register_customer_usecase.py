from app.domain.value_objects import CPF, Email

from app.application.gateways.data.customer_data_provider import CustomerDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase
from app.domain.entities.customer_entity import CustomerEntity
from app.domain.exceptions import CustomerAlreadyExistsException


class RegisterCustomerUseCase(BaseUseCase):

    def __init__(self, customer_data_provider: CustomerDataProviderInterface):
        self._customer_data_provider = customer_data_provider

    def _validate_already_exists(self, cpf: str) -> CustomerAlreadyExistsException | bool:
        customer = self._customer_data_provider.find_customer_by_cpf(cpf=cpf)
        if customer:
            raise CustomerAlreadyExistsException()
        return True

    def execute(self, **data) -> CustomerEntity:
        email = Email(data.get("email"))
        cpf = CPF(data.get("cpf"))
        name = data.get("name")

        self._validate_already_exists(cpf=cpf.value)

        customer = CustomerEntity(name=name, cpf=cpf, email=email)
        customer_data_provider = self._customer_data_provider.create(customer)
        customer.id = customer_data_provider.id

        return customer
