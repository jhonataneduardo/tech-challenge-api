from typing import Optional
from pydantic import BaseModel

from app.domain.entities.category_entity import CategoryEntity


class OutputCategoryDTO(BaseModel):
    id: int
    name: str
    created_at: str
    updated_at: Optional[str] = None

    @classmethod
    def from_domain(cls, category: CategoryEntity):
        return cls(
            id=category.id,
            name=category.name,
            created_at=category.created_at.strftime(format="%Y-%m-%dT%H:%M:%SZ"),
            updated_at=category.updated_at.strftime(format="%Y-%m-%dT%H:%M:%SZ") if category.updated_at else None
        )

    def to_dict(self):
        return self.model_dump(exclude_none=True)
