from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.dice as dice
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.uuid as uuid


@dataclass(slots=True)
class MemoryAccount:
    iD: Optional[ID] = field(default_factory=ID)
    alterIDs: Optional[list[ID]] = field(default_factory=list[ID])
    security: Optional[SecurityType] = field(default_factory=SecurityType)
    authenticatedLengthExperiment: Optional[bool] = None
    noTerminationSignal: Optional[bool] = None
