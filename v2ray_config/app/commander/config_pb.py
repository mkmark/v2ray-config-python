from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    tag: Optional[str] = None
    service: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class ReflectionConfig:
    pass


@dataclass(slots=True)
class SimplifiedConfig:
    tag: Optional[str] = None
    name: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class x:
    pass
