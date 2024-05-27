from typing import Dict, Optional
from dataclasses import dataclass, asdict

from app.domain.entities.base import AggregateRoot
from app.domain.entities.category_entity import CategoryEntity


@dataclass(slots=True)
class ProductEntity(AggregateRoot):
    name: str
    description: str
    price: float
    category: CategoryEntity

    def as_dict(self) -> Dict:
        serialized = asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
        return serialized

    @classmethod
    def from_dict(cls, data: Dict):
        data_copy = data
        data_copy["category"] = CategoryEntity.from_dict(data=data["category"])
        return cls(**data_copy)


@dataclass(frozen=True)
class ProductEntityFilter:
    category_id: Optional[int] = None
