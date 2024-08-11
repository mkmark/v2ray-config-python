from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.serial as serial


@dataclass(slots=True)
class TransportProtocol(int):
    pass


@dataclass(slots=True)
class DomainStrategy(int):
    pass


@dataclass(slots=True)
class SocketConfig_TProxyMode(int):
    pass


@dataclass(slots=True)
class TransportConfig:
    protocol: Optional[TransportProtocol] = field(default_factory=TransportProtocol)
    protocol_name: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class ProxyConfig:
    tag: Optional[str] = None
    transportLayerProxy: Optional[bool] = None


@dataclass(slots=True)
class CustomSockopt:
    level: Optional[str] = None
    opt: Optional[str] = None
    value: Optional[str] = None
    type: Optional[str] = None


@dataclass(slots=True)
class SocketConfig:
    mark: Optional[int] = None
    tfo: Optional[int] = None
    tproxy: Optional[SocketConfig_TProxyMode] = field(
        default_factory=SocketConfig_TProxyMode
    )
    receive_original_dest_address: Optional[bool] = None
    bind_address: Optional[list[int]] = field(default_factory=list[int])
    bind_port: Optional[int] = None
    accept_proxy_protocol: Optional[bool] = None
    domain_strategy: Optional[DomainStrategy] = field(default_factory=DomainStrategy)
    dialer_proxy: Optional[str] = None
    tcp_keep_alive_interval: Optional[int] = None
    tcp_keep_alive_idle: Optional[int] = None
    tcp_congestion: Optional[str] = None
    interface: Optional[str] = None
    v6only: Optional[bool] = None
    tcp_window_clamp: Optional[int] = None
    tcp_user_timeout: Optional[int] = None
    tcp_max_seg: Optional[int] = None
    tcp_no_delay: Optional[bool] = None
    tcp_mptcp: Optional[bool] = None
    customSockopt: Optional[list[CustomSockopt]] = field(
        default_factory=list[CustomSockopt]
    )


@dataclass(slots=True)
class StreamConfig:
    protocol: Optional[TransportProtocol] = field(default_factory=TransportProtocol)
    protocol_name: Optional[str] = None
    transport_settings: Optional[list[TransportConfig]] = field(
        default_factory=list[TransportConfig]
    )
    security_type: Optional[str] = None
    security_settings: Optional[list[dict]] = field(default_factory=list[dict])
    socket_settings: Optional[SocketConfig] = field(default_factory=SocketConfig)


@dataclass(slots=True)
class x:
    pass
