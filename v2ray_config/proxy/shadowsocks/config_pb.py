from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class CipherType(int):
    pass


@dataclass(slots=True)
class Account:
    password: Optional[str] = None
    cipher_type: Optional[CipherType] = field(default_factory=CipherType)
    iv_check: Optional[bool] = None
    experiment_reduced_iv_head_entropy: Optional[bool] = None


@dataclass(slots=True)
class ServerConfig:
    udp_enabled: Optional[bool] = None
    user: Optional[User] = field(default_factory=User)
    network: Optional[list[str]] = field(default_factory=list[str])
    packet_encoding: Optional[str] = None


@dataclass(slots=True)
class ClientConfig:
    server: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])


@dataclass(slots=True)
class x:
    pass
