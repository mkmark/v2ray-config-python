from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    header_settings: Optional[Any] = field(default_factory=Any)
    accept_proxy_protocol: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
