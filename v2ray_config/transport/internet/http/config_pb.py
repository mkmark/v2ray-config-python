from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext
# import v2ray_config.transport.internet.headers.http as http


@dataclass(slots=True)
class Config:
    host: Optional[list[str]] = field(default_factory=list[str])
    path: Optional[str] = None
    method: Optional[str] = None
    header: Optional[list[Header]] = field(default_factory=list[Header])


@dataclass(slots=True)
class x:
    pass
