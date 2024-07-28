from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Control_State(int):
    pass


@dataclass(slots=True)
class Control:
    random: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class BridgeConfig:
    tag: Optional[str] = None
    domain: Optional[str] = None


@dataclass(slots=True)
class PortalConfig:
    tag: Optional[str] = None
    domain: Optional[str] = None


@dataclass(slots=True)
class Config:
    bridge_config: Optional[list[BridgeConfig]] = field(default_factory=list[BridgeConfig])
    portal_config: Optional[list[PortalConfig]] = field(default_factory=list[PortalConfig])


@dataclass(slots=True)
class x:
    pass
