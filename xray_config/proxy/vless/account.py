from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.common.uuid as uuid


@dataclass(slots=True)
class MemoryAccount:
    iD: Optional[ID] = field(default_factory=ID)
    flow: Optional[str] = None
    encryption: Optional[str] = None
