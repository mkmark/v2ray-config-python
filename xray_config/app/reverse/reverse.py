from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.core as core
# import xray_config.features.outbound as outbound
# import xray_config.features.routing as routing


@dataclass(slots=True)
class Reverse:
    bridges: Optional[list[Bridge]] = field(default_factory=list[Bridge])
    portals: Optional[list[Portal]] = field(default_factory=list[Portal])
