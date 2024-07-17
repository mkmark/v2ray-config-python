from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.tun.device as device


@dataclass(slots=True)
class GvisorTUN(LinkEndpoint):
    options: Optional[Options] = field(default_factory=Options)
    fd: Optional[int] = None
    mtu: Optional[int] = None
