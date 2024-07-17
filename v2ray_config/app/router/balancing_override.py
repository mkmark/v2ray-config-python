from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class overrideSettings:
    target: Optional[str] = None


@dataclass(slots=True)
class override:
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    settings: Optional[overrideSettings] = field(default_factory=overrideSettings)
