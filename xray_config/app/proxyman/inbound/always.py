from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.proxyman as proxyman
# import xray_config.common as common
# import xray_config.common.dice as dice
# import xray_config.common.errors as errors
# import xray_config.common.mux as mux
# import xray_config.common.net as net
# import xray_config.core as core
# import xray_config.features.policy as policy
# import xray_config.features.stats as stats
# import xray_config.proxy as proxy
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class AlwaysOnInboundHandler:
    proxy: Optional[Inbound] = field(default_factory=Inbound)
    workers: Optional[list[worker]] = field(default_factory=list[worker])
    mux: Optional[Server] = field(default_factory=Server)
    tag: Optional[str] = None
