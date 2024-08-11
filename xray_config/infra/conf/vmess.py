from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial
# import xray_config.common.uuid as uuid
# import xray_config.proxy.vmess as vmess
# import xray_config.proxy.vmess.inbound as inbound
# import xray_config.proxy.vmess.outbound as outbound


@dataclass(slots=True)
class VMessAccount:
    id: Optional[str] = None
    security: Optional[str] = None
    experiments: Optional[str] = None


@dataclass(slots=True)
class VMessDetourConfig:
    to: Optional[str] = None


@dataclass(slots=True)
class FeaturesConfig:
    detour: Optional[VMessDetourConfig] = field(default_factory=VMessDetourConfig)


@dataclass(slots=True)
class VMessDefaultConfig:
    level: Optional[int] = None


@dataclass(slots=True)
class VMessInboundConfig:
    clients: Optional[list[dict]] = field(default_factory=list[dict])
    features: Optional[FeaturesConfig] = field(default_factory=FeaturesConfig)
    default: Optional[VMessDefaultConfig] = field(default_factory=VMessDefaultConfig)
    detour: Optional[VMessDetourConfig] = field(default_factory=VMessDetourConfig)


@dataclass(slots=True)
class VMessOutboundTarget:
    address: Optional[str] = None
    port: Optional[int] = None
    users: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class VMessOutboundConfig:
    vnext: Optional[list[VMessOutboundTarget]] = field(default_factory=list[VMessOutboundTarget])
