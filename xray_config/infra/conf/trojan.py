from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial
# import xray_config.proxy.trojan as trojan


@dataclass(slots=True)
class TrojanServerTarget:
    address: Optional[str] = None
    port: Optional[int] = None
    password: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = None
    flow: Optional[str] = None


@dataclass(slots=True)
class TrojanClientConfig:
    servers: Optional[list[TrojanServerTarget]] = field(default_factory=list[TrojanServerTarget])


@dataclass(slots=True)
class TrojanInboundFallback:
    name: Optional[str] = None
    alpn: Optional[str] = None
    path: Optional[str] = None
    type: Optional[str] = None
    dest: Optional[dict] = field(default_factory=dict)
    xver: Optional[int] = None


@dataclass(slots=True)
class TrojanUserConfig:
    password: Optional[str] = None
    level: Optional[int] = None
    email: Optional[str] = None
    flow: Optional[str] = None


@dataclass(slots=True)
class TrojanServerConfig:
    clients: Optional[list[TrojanUserConfig]] = field(default_factory=list[TrojanUserConfig])
    fallback: Optional[TrojanInboundFallback] = field(default_factory=TrojanInboundFallback)
    fallbacks: Optional[list[TrojanInboundFallback]] = field(default_factory=list[TrojanInboundFallback])
