from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.features.routing as routing
# import v2ray_config.features.stats as stats


@dataclass(slots=True)
class routingServer:
    router: Optional[Router] = field(default_factory=Router)
    routingStats: Optional[Channel] = field(default_factory=Channel)


@dataclass(slots=True)
class service:
    v: Optional[Instance] = field(default_factory=Instance)
