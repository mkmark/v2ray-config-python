from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    tag: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
