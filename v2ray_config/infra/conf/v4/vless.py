from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.proxy.vless as vless
# import v2ray_config.proxy.vless.inbound as inbound
# import v2ray_config.proxy.vless.outbound as outbound


@dataclass(slots=True)
class VLessInboundFallback:
    alpn: Optional[str] = None
    path: Optional[str] = None
    type: Optional[str] = None
    dest: Optional[dict] = field(default_factory=dict)
    xver: Optional[int] = None


@dataclass(slots=True)
class VLessInboundConfig:
    clients: Optional[list[dict]] = field(default_factory=list[dict])
    decryption: Optional[str] = None
    fallback: Optional[dict] = field(default_factory=dict)
    fallbacks: Optional[list[VLessInboundFallback]] = field(default_factory=list[VLessInboundFallback])


@dataclass(slots=True)
class VLessOutboundVnext:
    address: Optional[str] = None
    port: Optional[int] = None
    users: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class VLessOutboundConfig:
    vnext: Optional[list[VLessOutboundVnext]] = field(default_factory=list[VLessOutboundVnext])
