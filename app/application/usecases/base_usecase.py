from abc import ABC, abstractmethod
from typing import TypeVar

IN = TypeVar('IN')
OUT = TypeVar('OUT')


class BaseUseCase(ABC):

    @abstractmethod
    def execute(self, **input_data: IN) -> OUT:
        raise NotImplementedError
