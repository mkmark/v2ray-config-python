from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.grpc.encoding as encoding
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Listener(UnimplementedGunServiceServer):
    ctx: Optional[Context] = field(default_factory=Context)
    handler: Optional[ConnHandler] = field(default_factory=ConnHandler)
    local: Optional[Addr] = field(default_factory=Addr)
    config: Optional[Config] = field(default_factory=Config)
    s: Optional[Server] = field(default_factory=Server)
