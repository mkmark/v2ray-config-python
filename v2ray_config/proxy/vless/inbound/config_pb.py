from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.common.protocol.user_pb import User

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Fallback:
    alpn: Optional[str] = None
    path: Optional[str] = None
    type: Optional[str] = None
    dest: Optional[str] = None
    xver: Optional[int] = None


@dataclass(slots=True)
class Config:
    clients: Optional[list[User]] = field(default_factory=list[User])
    decryption: Optional[str] = None
    fallbacks: Optional[list[Fallback]] = field(default_factory=list[Fallback])


@dataclass(slots=True)
class SimplifiedConfig:
    users: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class x:
    pass
