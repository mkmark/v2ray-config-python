from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class DetourConfig:
    to: Optional[str] = None


@dataclass(slots=True)
class DefaultConfig:
    level: Optional[int] = None


@dataclass(slots=True)
class Config:
    user: Optional[list[User]] = field(default_factory=list[User])
    default: Optional[DefaultConfig] = field(default_factory=DefaultConfig)
    detour: Optional[DetourConfig] = field(default_factory=DetourConfig)


@dataclass(slots=True)
class x:
    pass
