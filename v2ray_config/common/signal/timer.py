from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.task as task


@dataclass(slots=True)
class ActivityTimer(RWMutex):
    updated: Optional[chan] = field(default_factory=chan)
    check_task: Optional[Periodic] = field(default_factory=Periodic)
