from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class lru:
    capacity: Optional[int] = None
    double_linkedlist: Optional[List] = field(default_factory=List)
    key_to_element: Optional[Map] = field(default_factory=Map)
    value_to_element: Optional[Map] = field(default_factory=Map)
    mu: Optional[Mutex] = field(default_factory=Mutex)


@dataclass(slots=True)
class lruElement:
    key: Optional[dict] = field(default_factory=dict)
    value: Optional[dict] = field(default_factory=dict)
