from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.uuid as uuid


@dataclass(slots=True)
class MemoryAccount:
    iD: Optional[ID] = field(default_factory=ID)
    flow: Optional[str] = None
    encryption: Optional[str] = None
