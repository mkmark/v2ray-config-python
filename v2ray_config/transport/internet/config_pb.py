from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class TransportProtocol(int):
    pass


@dataclass(slots=True)
class SocketConfig_TCPFastOpenState(int):
    pass


@dataclass(slots=True)
class SocketConfig_TProxyMode(int):
    pass


@dataclass(slots=True)
class TransportConfig:
    protocol: Optional[TransportProtocol] = field(default_factory=TransportProtocol)
    protocol_name: Optional[str] = None
    settings: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class StreamConfig:
    protocol: Optional[TransportProtocol] = field(default_factory=TransportProtocol)
    protocol_name: Optional[str] = None
    transport_settings: Optional[list[TransportConfig]] = field(default_factory=list[TransportConfig])
    security_type: Optional[str] = None
    security_settings: Optional[list[Any]] = field(default_factory=list[Any])
    socket_settings: Optional[SocketConfig] = field(default_factory=SocketConfig)


@dataclass(slots=True)
class ProxyConfig:
    tag: Optional[str] = None
    transportLayerProxy: Optional[bool] = None


@dataclass(slots=True)
class SocketConfig:
    mark: Optional[int] = None
    tfo: Optional[SocketConfig_TCPFastOpenState] = field(default_factory=SocketConfig_TCPFastOpenState)
    tproxy: Optional[SocketConfig_TProxyMode] = field(default_factory=SocketConfig_TProxyMode)
    receive_original_dest_address: Optional[bool] = None
    bind_address: Optional[list[int]] = field(default_factory=list[int])
    bind_port: Optional[int] = None
    accept_proxy_protocol: Optional[bool] = None
    tcp_keep_alive_interval: Optional[int] = None
    tfo_queue_length: Optional[int] = None
    tcp_keep_alive_idle: Optional[int] = None
    bind_to_device: Optional[str] = None
    rx_buf_size: Optional[int] = None
    tx_buf_size: Optional[int] = None
    force_buf_size: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
