from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class SessionConfig:
    pass


@dataclass(slots=True)
class Config:
    settings: Optional[SessionConfig] = field(default_factory=SessionConfig)


@dataclass(slots=True)
class x:
    pass
