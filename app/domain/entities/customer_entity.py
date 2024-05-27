from typing import Dict
from dataclasses import dataclass, asdict

from app.domain.entities.base import AggregateRoot
from app.domain.value_objects import CPF, Email


@dataclass
class CustomerEntity(AggregateRoot):
    name: str
    email: Email
    cpf: CPF

    def as_dict(self) -> Dict:
        serialized = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        serialized["email"] = self.email.value
        serialized["cpf"] = self.cpf.value
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        data_copy["email"] = Email(data["email"])
        data_copy["cpf"] = CPF(data["cpf"])
        return cls(**data_copy)
