from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class PortRange:
    from_: Optional[int] = None
    to: Optional[int] = None


@dataclass(slots=True)
class PortList:
    range: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class x:
    pass
