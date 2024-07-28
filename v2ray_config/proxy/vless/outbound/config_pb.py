from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    vnext: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])


@dataclass(slots=True)
class SimplifiedConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    uuid: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
