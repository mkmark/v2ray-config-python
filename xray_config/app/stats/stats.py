from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.features.stats as stats


@dataclass(slots=True)
class Manager:
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    counters: Optional[dict[str, Counter]] = field(default_factory=dict[str, Counter])
    channels: Optional[dict[str, Channel]] = field(default_factory=dict[str, Channel])
    running: Optional[bool] = None
