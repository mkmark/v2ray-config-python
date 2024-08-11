from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class CipherType(int):
    pass


@dataclass(slots=True)
class Account:
    password: Optional[str] = None
    cipher_type: Optional[CipherType] = field(default_factory=CipherType)
    iv_check: Optional[bool] = None


@dataclass(slots=True)
class ServerConfig:
    users: Optional[list[User]] = field(default_factory=list[User])
    network: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class ClientConfig:
    server: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])


@dataclass(slots=True)
class x:
    pass
