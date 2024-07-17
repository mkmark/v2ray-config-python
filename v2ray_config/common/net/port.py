from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Port(int):
    pass


@dataclass(slots=True)
class MemoryPortRange:
    from_: Optional[int] = None
    to: Optional[int] = None


@dataclass(slots=True)
class MemoryPortList(list[MemoryPortRange]):
    pass
