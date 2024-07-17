from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.tun.net as net
# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.log as log
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class tcpConn(TCPConn):
    id: Optional[TransportEndpointID] = field(default_factory=TransportEndpointID)


@dataclass(slots=True)
class TCPHandler:
    ctx: Optional[Context] = field(default_factory=Context)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    policy_manager: Optional[Manager] = field(default_factory=Manager)
    config: Optional[Config] = field(default_factory=Config)
