from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.stats as stats
# import v2ray_config.common as common
# import v2ray_config.common.strmatcher as strmatcher
# import v2ray_config.features.stats as stats


@dataclass(slots=True)
class statsServer:
    stats: Optional[Manager] = field(default_factory=Manager)
    startTime: Optional[Time] = field(default_factory=Time)


@dataclass(slots=True)
class service:
    statsManager: Optional[Manager] = field(default_factory=Manager)
