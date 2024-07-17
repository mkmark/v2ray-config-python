from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.common as common
# import v2ray_config.common.dice as dice
# import v2ray_config.common.errors as errors
# import v2ray_config.common.mux as mux
# import v2ray_config.common.net as net
# import v2ray_config.features.policy as policy
# import v2ray_config.features.stats as stats
# import v2ray_config.proxy as proxy
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class AlwaysOnInboundHandler:
    proxy: Optional[Inbound] = field(default_factory=Inbound)
    workers: Optional[list[worker]] = field(default_factory=list[worker])
    mux: Optional[Server] = field(default_factory=Server)
    tag: Optional[str] = None
