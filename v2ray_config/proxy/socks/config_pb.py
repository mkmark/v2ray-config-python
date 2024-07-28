from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class AuthType(int):
    pass


@dataclass(slots=True)
class Version(int):
    pass


@dataclass(slots=True)
class Account:
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass(slots=True)
class ServerConfig:
    auth_type: Optional[AuthType] = field(default_factory=AuthType)
    accounts: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    address: Optional[str] = None
    udp_enabled: Optional[bool] = None
    timeout: Optional[int] = None
    user_level: Optional[int] = None
    packet_encoding: Optional[str] = None


@dataclass(slots=True)
class ClientConfig:
    server: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])
    version: Optional[Version] = field(default_factory=Version)
    delay_auth_write: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
