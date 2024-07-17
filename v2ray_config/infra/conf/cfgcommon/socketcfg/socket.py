from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class SocketConfig:
    mark: Optional[int] = None
    tcp_fast_open: Optional[bool] = None
    tproxy: Optional[str] = None
    accept_proxy_protocol: Optional[bool] = None
    tcp_keep_alive_interval: Optional[int] = None
    tcp_keep_alive_idle: Optional[int] = None
    tcp_fast_open_queue_length: Optional[int] = None
    bind_to_device: Optional[str] = None
    rx_buf_size: Optional[int] = None
    tx_buf_size: Optional[int] = None
    force_buf_size: Optional[bool] = None
