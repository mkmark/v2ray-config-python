from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.http as http
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.done as done
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener:
    server: Optional[Server] = field(default_factory=Server)
    handler: Optional[ConnHandler] = field(default_factory=ConnHandler)
    local: Optional[Addr] = field(default_factory=Addr)
    config: Optional[Config] = field(default_factory=Config)


@dataclass(slots=True)
class flushWriter:
    w: Optional[Writer] = field(default_factory=Writer)
    d: Optional[Instance] = field(default_factory=Instance)
