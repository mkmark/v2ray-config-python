from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.transport.internet.tagged as tagged


@dataclass(slots=True)
class pingClient:
    destination: Optional[str] = None
    httpClient: Optional[Client] = field(default_factory=Client)
