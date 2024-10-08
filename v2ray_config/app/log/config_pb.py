from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.log as log
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class LogType(int):
    pass


@dataclass(slots=True)
class LogSpecification:
    type: Optional[str] = None
    level: Optional[str] = None
    path: Optional[str] = None


@dataclass(slots=True)
class Config:
    error: Optional[LogSpecification] = field(default_factory=LogSpecification)
    access: Optional[LogSpecification] = field(default_factory=LogSpecification)


@dataclass(slots=True)
class x:
    pass
