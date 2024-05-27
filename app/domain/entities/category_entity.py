from typing import Dict
from dataclasses import dataclass, asdict

from app.domain.entities.base import AggregateRoot


@dataclass(slots=True)
class CategoryEntity(AggregateRoot):
    name: str

    def as_dict(self) -> Dict:
        serialized = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        return cls(**data_copy)
