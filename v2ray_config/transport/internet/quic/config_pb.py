from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    key: Optional[str] = None
    security: Optional[SecurityConfig] = field(default_factory=SecurityConfig)
    header: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class x:
    pass
