from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ServerConfig:
    users: Optional[list[str]] = field(default_factory=list[str])
    packet_encoding: Optional[str] = None


@dataclass(slots=True)
class ClientConfig:
    address: Optional[str] = None
    port: Optional[int] = None
    password: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
