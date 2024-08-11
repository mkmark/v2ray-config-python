from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.grpc.encoding as encoding
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener(UnimplementedGRPCServiceServer):
    ctx: Optional[Context] = field(default_factory=Context)
    handler: Optional[ConnHandler] = field(default_factory=ConnHandler)
    local: Optional[Addr] = field(default_factory=Addr)
    config: Optional[Config] = field(default_factory=Config)
    s: Optional[Server] = field(default_factory=Server)
