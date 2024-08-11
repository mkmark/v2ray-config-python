from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Fallback:
    name: Optional[str] = None
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
class x:
    pass
