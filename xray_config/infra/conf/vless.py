from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial
# import xray_config.common.uuid as uuid
# import xray_config.proxy.vless as vless
# import xray_config.proxy.vless.inbound as inbound
# import xray_config.proxy.vless.outbound as outbound


@dataclass(slots=True)
class VLessInboundFallback:
    name: Optional[str] = None
    alpn: Optional[str] = None
    path: Optional[str] = None
    type: Optional[str] = None
    dest: Optional[dict] = field(default_factory=dict)
    xver: Optional[int] = None


@dataclass(slots=True)
class VLessInboundConfig:
    clients: Optional[list[dict]] = field(default_factory=list[dict])
    decryption: Optional[str] = None
    fallback: Optional[VLessInboundFallback] = field(default_factory=VLessInboundFallback)
    fallbacks: Optional[list[VLessInboundFallback]] = field(default_factory=list[VLessInboundFallback])


@dataclass(slots=True)
class VLessOutboundVnext:
    address: Optional[str] = None
    port: Optional[int] = None
    users: Optional[list[dict]] = field(default_factory=list[dict])


@dataclass(slots=True)
class VLessOutboundConfig:
    vnext: Optional[list[VLessOutboundVnext]] = field(default_factory=list[VLessOutboundVnext])
