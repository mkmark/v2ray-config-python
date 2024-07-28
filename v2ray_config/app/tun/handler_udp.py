from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.tun.net as net
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.udp as udp
# import v2ray_config.common.session as session
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing
# import v2ray_config.transport.internet.udp as udp


@dataclass(slots=True)
class UDPHandler:
    ctx: Optional[Context] = field(default_factory=Context)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    policyManager: Optional[Manager] = field(default_factory=Manager)
    config: Optional[Config] = field(default_factory=Config)


@dataclass(slots=True)
class udpConn(UDPConn):
    id: Optional[TransportEndpointID] = field(default_factory=TransportEndpointID)
