from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial


@dataclass(slots=True)
class Config:
    key: Optional[str] = None
    security: Optional[SecurityConfig] = field(default_factory=SecurityConfig)
    header: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class x:
    pass
