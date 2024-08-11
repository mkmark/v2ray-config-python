from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.common.protocol.server_spec_pb import ServerEndpoint

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Account:
    username: Optional[str] = None
    password: Optional[str] = None


@dataclass(slots=True)
class ServerConfig:
    timeout: Optional[int] = None
    accounts: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    allow_transparent: Optional[bool] = None
    user_level: Optional[int] = None


@dataclass(slots=True)
class Header:
    key: Optional[str] = None
    value: Optional[str] = None


@dataclass(slots=True)
class ClientConfig:
    server: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])
    header: Optional[list[Header]] = field(default_factory=list[Header])


@dataclass(slots=True)
class x:
    pass
