from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.platform.securedload as securedload
# import v2ray_config.features.extension as extension
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class Forwarder:
    ctx: Optional[Context] = field(default_factory=Context)
    forwarder: Optional[HTTPHandle] = field(default_factory=HTTPHandle)
    httpserver: Optional[Server] = field(default_factory=Server)
    config: Optional[Config] = field(default_factory=Config)
