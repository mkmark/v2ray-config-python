from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.reverse as reverse


@dataclass(slots=True)
class BridgeConfig:
    tag: Optional[str] = None
    domain: Optional[str] = None


@dataclass(slots=True)
class PortalConfig:
    tag: Optional[str] = None
    domain: Optional[str] = None


@dataclass(slots=True)
class ReverseConfig:
    bridges: Optional[list[BridgeConfig]] = field(default_factory=list[BridgeConfig])
    portals: Optional[list[PortalConfig]] = field(default_factory=list[PortalConfig])
