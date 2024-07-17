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
    tcp_settings: Optional[TCPConfig] = field(default_factory=TCPConfig)
    kcp_settings: Optional[KCPConfig] = field(default_factory=KCPConfig)
    ws_settings: Optional[WebSocketConfig] = field(default_factory=WebSocketConfig)
    http_settings: Optional[HTTPConfig] = field(default_factory=HTTPConfig)
    ds_settings: Optional[DomainSocketConfig] = field(
        default_factory=DomainSocketConfig
    )
    quic_settings: Optional[QUICConfig] = field(default_factory=QUICConfig)
    gun_settings: Optional[GunConfig] = field(default_factory=GunConfig)
    grpc_settings: Optional[GunConfig] = field(default_factory=GunConfig)
