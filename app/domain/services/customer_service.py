from typing import Optional, List

from app.domain.interfaces.repositories.customer_repository_interface import CustomerRepositoryInterface
from app.domain.entities.customer_entity import CustomerEntity
from app.domain.value_objects import CPF, Email

from app.domain.exceptions import CustomerAlreadyExistsException, CustomerNotFoundException, EntityNotFoundException


class CustomerService:

    def __init__(self, repository: CustomerRepositoryInterface) -> None:
        self._repository = repository

    def _validate_already_exists(self, cpf: str) -> CustomerAlreadyExistsException | bool:
        customer = self._repository.find_customer_by_cpf(cpf=cpf)
        if customer:
            raise CustomerAlreadyExistsException()
        return True

    def create_customer(self, name: str, cpf: str, email: str) -> Optional[CustomerEntity]:
        # Validations
        email = Email(email)
        cpf = CPF(cpf)
        self._validate_already_exists(cpf=cpf.value)
        entity = CustomerEntity(name=name, cpf=cpf, email=email)
        model = self._repository.create(customer_entity=entity)
        entity.id = model.id
        return entity

    def all_customers(self) -> List[CustomerEntity]:
        categories = self._repository.list()
        if not categories:
            raise EntityNotFoundException("There are no registered customers.")
        return categories

    def find_customer_by_cpf(self, cpf: str) -> Optional[CustomerEntity]:
        result = self._repository.find_customer_by_cpf(cpf=CPF(cpf).value)
        if not result:
            raise CustomerNotFoundException()
        return CustomerEntity.from_dict(result)
