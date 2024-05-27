from datetime import datetime
from dataclasses import field, dataclass


@dataclass
class Entity:
    id: int = field(default=None, repr=False, kw_only=True)
    created_at: datetime = field(default=datetime.now(), kw_only=True)
    updated_at: datetime = field(default=None, kw_only=True)


class AggregateRoot(Entity):
    pass
