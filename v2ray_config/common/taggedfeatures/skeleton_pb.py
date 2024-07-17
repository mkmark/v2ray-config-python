from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    features: Optional[dict[str, Any]] = field(default_factory=dict[str, Any])


@dataclass(slots=True)
class x:
    pass
