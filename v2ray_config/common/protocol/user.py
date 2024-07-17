from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class MemoryUser:
    account: Optional[Account] = field(default_factory=Account)
    email: Optional[str] = None
    level: Optional[int] = None
