from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class ProxyConfig:
    tag: Optional[str] = None
    transportLayer: Optional[bool] = None
