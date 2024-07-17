from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.signal.done as done
# import v2ray_config.common.task as task


@dataclass(slots=True)
class Subscriber:
    buffer: Optional[chan] = field(default_factory=chan)
    done: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class Service(RWMutex):
    subs: Optional[dict[string][, Subscriber]] = field(default_factory=dict[string][, Subscriber])
    ctask: Optional[Periodic] = field(default_factory=Periodic)
