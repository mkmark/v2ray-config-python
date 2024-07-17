from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.environment as environment
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class systemDefaultDialer:
    pass


@dataclass(slots=True)
class systemNetworkImpl:
    listener: Optional[SystemListener] = field(default_factory=SystemListener)
    dialer: Optional[SystemDialer] = field(default_factory=SystemDialer)


@dataclass(slots=True)
class systemListenerWithDefaultOpt(SystemListener):
    opt: Optional[SocketConfig] = field(default_factory=SocketConfig)


@dataclass(slots=True)
class systemDialerWithDefaultOpt(SystemDialer):
    opt: Optional[SocketConfig] = field(default_factory=SocketConfig)
