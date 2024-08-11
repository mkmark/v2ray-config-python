from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class lru:
    capacity: Optional[int] = None
    doubleLinkedlist: Optional[List] = field(default_factory=List)
    keyToElement: Optional[Map] = field(default_factory=Map)
    valueToElement: Optional[Map] = field(default_factory=Map)
    mu: Optional[Mutex] = field(default_factory=Mutex)


@dataclass(slots=True)
class lruElement:
    key: Optional[dict] = field(default_factory=dict)
    value: Optional[dict] = field(default_factory=dict)
