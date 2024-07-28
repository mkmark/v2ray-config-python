from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class SocketConfig:
    mark: Optional[int] = None
    tcpFastOpen: Optional[bool] = None
    tproxy: Optional[str] = None
    acceptProxyProtocol: Optional[bool] = None
    tcpKeepAliveInterval: Optional[int] = None
    tcpKeepAliveIdle: Optional[int] = None
    tcpFastOpenQueueLength: Optional[int] = None
    bindToDevice: Optional[str] = None
    rxBufSize: Optional[int] = None
    txBufSize: Optional[int] = None
    forceBufSize: Optional[bool] = None
