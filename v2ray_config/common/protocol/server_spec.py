from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.dice as dice
# import v2ray_config.common.net as net


@dataclass(slots=True)
class alwaysValidStrategy:
    pass


@dataclass(slots=True)
class timeoutValidStrategy:
    until: Optional[Time] = field(default_factory=Time)


@dataclass(slots=True)
class ServerSpec(RWMutex):
    dest: Optional[Destination] = field(default_factory=Destination)
    users: Optional[list[MemoryUser]] = field(default_factory=list[MemoryUser])
    valid: Optional[ValidationStrategy] = field(default_factory=ValidationStrategy)
