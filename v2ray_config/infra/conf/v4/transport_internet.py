from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.infra.conf.cfgcommon.socketcfg.socket import SocketConfig
from v2ray_config.infra.conf.cfgcommon.tlscfg.tls import TLSConfig
from v2ray_config.infra.conf.v4.gun import GunConfig

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.cfgcommon.loader as loader
# import v2ray_config.infra.conf.cfgcommon.socketcfg as socketcfg
# import v2ray_config.infra.conf.cfgcommon.tlscfg as tlscfg
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.domainsocket as domainsocket
# import v2ray_config.transport.internet.headers.http as http
# import v2ray_config.transport.internet.http as http
# import v2ray_config.transport.internet.kcp as kcp
# import v2ray_config.transport.internet.quic as quic
# import v2ray_config.transport.internet.tcp as tcp
# import v2ray_config.transport.internet.websocket as websocket


@dataclass(slots=True)
class TransportProtocol(str):
    pass


@dataclass(slots=True)
class KCPConfig:
    mtu: Optional[int] = None
    tti: Optional[int] = None
    uplink_capacity: Optional[int] = None
    downlink_capacity: Optional[int] = None
    congestion: Optional[bool] = None
    read_buffer_size: Optional[int] = None
    write_buffer_size: Optional[int] = None
    header: Optional[dict] = field(default_factory=dict)
    seed: Optional[str] = None


@dataclass(slots=True)
class TCPConfig:
    header: Optional[dict] = field(default_factory=dict)
    accept_proxy_protocol: Optional[bool] = None


@dataclass(slots=True)
class WebSocketConfig:
    path: Optional[str] = None
    headers: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    accept_proxy_protocol: Optional[bool] = None
    max_early_data: Optional[int] = None
    use_browser_forwarding: Optional[bool] = None
    early_data_header_name: Optional[str] = None


@dataclass(slots=True)
class HTTPConfig:
    host: Optional[list[str]] = field(default_factory=list[str])
    path: Optional[str] = None
    method: Optional[str] = None
    headers: Optional[dict[str, list[str]]] = field(
        default_factory=dict[str, list[str]]
    )


@dataclass(slots=True)
class QUICConfig:
    header: Optional[dict] = field(default_factory=dict)
    security: Optional[str] = None
    key: Optional[str] = None


@dataclass(slots=True)
class DomainSocketConfig:
    path: Optional[str] = None
    abstract: Optional[bool] = None
    padding: Optional[bool] = None


@dataclass(slots=True)
class StreamConfig:
    network: Optional[str] = None
    security: Optional[str] = None
    tls_settings: Optional[TLSConfig] = field(default_factory=TLSConfig)
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
    sockopt: Optional[SocketConfig] = field(default_factory=SocketConfig)
