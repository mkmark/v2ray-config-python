from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.common.protocol.server_spec_pb import ServerEndpoint
from xray_config.infra.conf.common import User

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Account:
    password: Optional[str] = None


@dataclass(slots=True)
class Fallback:
    name: Optional[str] = None
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


@dataclass(slots=True)
class x:
    pass
