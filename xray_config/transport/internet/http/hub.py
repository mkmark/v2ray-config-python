from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.protocol.http as http
# import xray_config.common.serial as serial
# import xray_config.common.signal.done as done
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.tls as tls


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
