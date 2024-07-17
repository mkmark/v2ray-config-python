from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.common.net.packetaddr.config_pb import PacketAddrType
from v2ray_config.common.protocol.server_spec_pb import ServerEndpoint
from v2ray_config.common.protocol.user_pb import User

# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class Account:
    password: Optional[str] = None


@dataclass(slots=True)
class Fallback:
    alpn: Optional[str] = None
    path: Optional[str] = None
    type: Optional[str] = None
    dest: Optional[str] = None
    xver: Optional[int] = None


@dataclass(slots=True)
class ClientConfig:
    server: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])


@dataclass(slots=True)
class ServerConfig:
    users: Optional[list[User]] = field(default_factory=list[User])
    fallbacks: Optional[list[Fallback]] = field(default_factory=list[Fallback])
    packet_encoding: Optional[PacketAddrType] = field(default_factory=PacketAddrType)


@dataclass(slots=True)
class x:
    pass
