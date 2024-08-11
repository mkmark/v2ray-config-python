from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Addons:
    flow: Optional[str] = None
    seed: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class x:
    pass
