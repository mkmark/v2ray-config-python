from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.tun.device as device
# import v2ray_config.app.tun.device.gvisor as gvisor
# import v2ray_config.app.tun.tunsorter as tunsorter
# import v2ray_config.common as common
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class TUN:
    ctx: Optional[Context] = field(default_factory=Context)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    policy_manager: Optional[Manager] = field(default_factory=Manager)
    config: Optional[Config] = field(default_factory=Config)
    stack: Optional[Stack] = field(default_factory=Stack)
