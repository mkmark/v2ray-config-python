from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class UDPFilter:
    ips: Optional[Map] = field(default_factory=Map)
