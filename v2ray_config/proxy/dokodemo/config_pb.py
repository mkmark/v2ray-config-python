from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    address: Optional[str] = None
    port: Optional[int] = None
    network_list: Optional[list[str]] = field(default_factory=list[str])
    networks: Optional[list[str]] = field(default_factory=list[str])
    timeout: Optional[int] = None
    follow_redirect: Optional[bool] = None
    user_level: Optional[int] = None


@dataclass(slots=True)
class SimplifiedConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    networks: Optional[list[str]] = field(default_factory=list[str])
    follow_redirect: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
