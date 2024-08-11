from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class SecurityType(int):
    pass


@dataclass(slots=True)
class SecurityConfig:
    type: Optional[SecurityType] = field(default_factory=SecurityType)


@dataclass(slots=True)
class x:
    pass
