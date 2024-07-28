from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.infra.conf.v4.gun import GunConfig
from v2ray_config.infra.conf.v4.transport_internet import (
    DomainSocketConfig,
    HTTPConfig,
    KCPConfig,
    QUICConfig,
    TCPConfig,
    WebSocketConfig,
)

# import v2ray_config.common.serial as serial
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class TransportConfig:
    tcpSettings: Optional[TCPConfig] = field(default_factory=TCPConfig)
    kcpSettings: Optional[KCPConfig] = field(default_factory=KCPConfig)
    wsSettings: Optional[WebSocketConfig] = field(default_factory=WebSocketConfig)
    httpSettings: Optional[HTTPConfig] = field(default_factory=HTTPConfig)
    dsSettings: Optional[DomainSocketConfig] = field(default_factory=DomainSocketConfig)
    quicSettings: Optional[QUICConfig] = field(default_factory=QUICConfig)
    gunSettings: Optional[GunConfig] = field(default_factory=GunConfig)
    grpcSettings: Optional[GunConfig] = field(default_factory=GunConfig)
