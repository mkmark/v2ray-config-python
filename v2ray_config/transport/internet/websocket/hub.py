from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.http as http
# import v2ray_config.common.session as session
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class requestHandler:
    path: Optional[str] = None
    ln: Optional[Listener] = field(default_factory=Listener)
    earlyDataEnabled: Optional[bool] = None
    earlyDataHeaderName: Optional[str] = None


@dataclass(slots=True)
class Listener(Mutex):
    server: Optional[Server] = field(default_factory=Server)
    listener: Optional[Listener] = field(default_factory=Listener)
    config: Optional[Config] = field(default_factory=Config)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
