from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.dice as dice
# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Validator(RWMutex):
    users: Optional[list[MemoryUser]] = field(default_factory=list[MemoryUser])
    behaviorSeed: Optional[int] = None
    behaviorFused: Optional[bool] = None
