from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.task as task


@dataclass(slots=True)
class ActivityTimer(RWMutex):
    updated: Optional[chan] = field(default_factory=chan)
    checkTask: Optional[Periodic] = field(default_factory=Periodic)
