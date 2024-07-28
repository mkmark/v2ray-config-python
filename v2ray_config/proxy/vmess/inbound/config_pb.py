from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class DetourConfig:
    to: Optional[str] = None


@dataclass(slots=True)
class DefaultConfig:
    alter_id: Optional[int] = None
    level: Optional[int] = None


@dataclass(slots=True)
class Config:
    user: Optional[list[User]] = field(default_factory=list[User])
    default: Optional[DefaultConfig] = field(default_factory=DefaultConfig)
    detour: Optional[DetourConfig] = field(default_factory=DetourConfig)
    secure_encryption_only: Optional[bool] = None


@dataclass(slots=True)
class SimplifiedConfig:
    users: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class x:
    pass
