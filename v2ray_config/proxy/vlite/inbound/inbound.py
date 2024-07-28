from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.environment as environment
# import v2ray_config.common.environment.envctx as envctx
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.done as done
# import v2ray_config.features.routing as routing
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class Handler:
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class status:
    config: Optional[UDPProtocolConfig] = field(default_factory=UDPProtocolConfig)
    password: Optional[list[int]] = field(default_factory=list[int])
    msgbus: Optional[Bus] = field(default_factory=Bus)
    ctx: Optional[Context] = field(default_factory=Context)
    transport: Optional[UnderlayTransportListener] = field(default_factory=UnderlayTransportListener)
    access: Optional[Mutex] = field(default_factory=Mutex)
