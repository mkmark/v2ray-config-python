from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.proxy.loopback as loopback


@dataclass(slots=True)
class LoopbackConfig:
    inbound_tag: Optional[str] = None
