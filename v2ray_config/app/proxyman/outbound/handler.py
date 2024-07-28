from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.common as common
# import v2ray_config.common.dice as dice
# import v2ray_config.common.environment as environment
# import v2ray_config.common.environment.envctx as envctx
# import v2ray_config.common.mux as mux
# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.features.dns as dns
# import v2ray_config.features.outbound as outbound
# import v2ray_config.features.policy as policy
# import v2ray_config.features.stats as stats
# import v2ray_config.proxy as proxy
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.security as security
# import v2ray_config.transport.pipe as pipe


@dataclass(slots=True)
class Handler:
    ctx: Optional[Context] = field(default_factory=Context)
    tag: Optional[str] = None
    senderSettings: Optional[SenderConfig] = field(default_factory=SenderConfig)
    streamSettings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    proxy: Optional[Outbound] = field(default_factory=Outbound)
    outboundManager: Optional[Manager] = field(default_factory=Manager)
    mux: Optional[ClientManager] = field(default_factory=ClientManager)
    uplinkCounter: Optional[Counter] = field(default_factory=Counter)
    downlinkCounter: Optional[Counter] = field(default_factory=Counter)
    dns: Optional[Client] = field(default_factory=Client)
