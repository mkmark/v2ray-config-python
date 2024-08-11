from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.core as core
# import xray_config.features.routing as routing
# import xray_config.features.stats as stats


@dataclass(slots=True)
class routingServer:
    router: Optional[Router] = field(default_factory=Router)
    routingStats: Optional[Channel] = field(default_factory=Channel)


@dataclass(slots=True)
class service:
    v: Optional[Instance] = field(default_factory=Instance)
