from typing import List

from app.application.gateways.data.customer_data_provider import CustomerDataProviderInterface
from app.application.usecases.base_usecase import BaseUseCase
from app.domain.entities.customer_entity import CustomerEntity
from app.domain.exceptions import EntityNotFoundException


class ListAllCustomersUseCase(BaseUseCase):

    def __init__(self, customer_data_provider: CustomerDataProviderInterface):
        self._customer_data_provider = customer_data_provider

    def execute(self) -> List[CustomerEntity]:
        categories = self._customer_data_provider.list()

        if not categories:
            raise EntityNotFoundException("There are no registered customers.")

        return categories
