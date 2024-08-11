from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.serial as serial


@dataclass(slots=True)
class Config:
    tag: Optional[str] = None
    listen: Optional[str] = None
    service: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class ReflectionConfig:
    pass


@dataclass(slots=True)
class x:
    pass
