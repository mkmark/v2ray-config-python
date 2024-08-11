from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.http as http
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class requestHandler:
    host: Optional[str] = None
    path: Optional[str] = None
    ln: Optional[Listener] = field(default_factory=Listener)


@dataclass(slots=True)
class Listener(Mutex):
    server: Optional[Server] = field(default_factory=Server)
    listener: Optional[Listener] = field(default_factory=Listener)
    config: Optional[Config] = field(default_factory=Config)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
