from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.stats as stats
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.strmatcher as strmatcher
# import xray_config.core as core
# import xray_config.features.stats as stats


@dataclass(slots=True)
class statsServer:
    stats: Optional[Manager] = field(default_factory=Manager)
    startTime: Optional[Time] = field(default_factory=Time)


@dataclass(slots=True)
class service:
    statsManager: Optional[Manager] = field(default_factory=Manager)
