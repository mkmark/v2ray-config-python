from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    host: Optional[str] = None
    service_name: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
