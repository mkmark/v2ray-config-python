from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.infra.conf.grpc import GRPCConfig
from xray_config.infra.conf.transport_internet import (
    DomainSocketConfig,
    HTTPConfig,
    HttpUpgradeConfig,
    KCPConfig,
    QUICConfig,
    SplitHTTPConfig,
    TCPConfig,
    WebSocketConfig,
)

# import xray_config.common.errors as errors
# import xray_config.common.serial as serial
# import xray_config.transport.global as global
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class TransportConfig:
    tcpSettings: Optional[TCPConfig] = field(default_factory=TCPConfig)
    kcpSettings: Optional[KCPConfig] = field(default_factory=KCPConfig)
    wsSettings: Optional[WebSocketConfig] = field(default_factory=WebSocketConfig)
    httpSettings: Optional[HTTPConfig] = field(default_factory=HTTPConfig)
    dsSettings: Optional[DomainSocketConfig] = field(default_factory=DomainSocketConfig)
    quicSettings: Optional[QUICConfig] = field(default_factory=QUICConfig)
    grpcSettings: Optional[GRPCConfig] = field(default_factory=GRPCConfig)
    gunSettings: Optional[GRPCConfig] = field(default_factory=GRPCConfig)
    httpupgradeSettings: Optional[HttpUpgradeConfig] = field(
        default_factory=HttpUpgradeConfig
    )
    splithttpSettings: Optional[SplitHTTPConfig] = field(
        default_factory=SplitHTTPConfig
    )
