from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class MemoryAccount:
    key: Optional[str] = None
    email: Optional[str] = None
    level: Optional[int] = None
