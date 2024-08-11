from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class dict:
    type: Optional[str] = None
    value: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class x:
    pass
