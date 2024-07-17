from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    listen_addr: Optional[str] = None
    listen_port: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
