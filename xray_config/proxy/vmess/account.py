from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.common.uuid as uuid


@dataclass(slots=True)
class MemoryAccount:
    iD: Optional[ID] = field(default_factory=ID)
    security: Optional[SecurityType] = field(default_factory=SecurityType)
    authenticatedLengthExperiment: Optional[bool] = None
    noTerminationSignal: Optional[bool] = None
