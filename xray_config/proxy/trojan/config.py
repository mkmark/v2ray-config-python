from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class MemoryAccount:
    password: Optional[str] = None
    key: Optional[list[int]] = field(default_factory=list[int])
