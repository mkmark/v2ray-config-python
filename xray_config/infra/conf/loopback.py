from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.proxy.loopback as loopback


@dataclass(slots=True)
class LoopbackConfig:
    inboundTag: Optional[str] = None
