from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.features.outbound as outbound
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class Reverse:
    bridges: Optional[list[Bridge]] = field(default_factory=list[Bridge])
    portals: Optional[list[Portal]] = field(default_factory=list[Portal])
