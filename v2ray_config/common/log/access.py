from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class logKey(int):
    pass


@dataclass(slots=True)
class AccessStatus(str):
    pass


@dataclass(slots=True)
class AccessMessage:
    from_: Optional[dict] = field(default_factory=dict)
    to: Optional[dict] = field(default_factory=dict)
    status: Optional[AccessStatus] = field(default_factory=AccessStatus)
    reason: Optional[dict] = field(default_factory=dict)
    email: Optional[str] = None
    detour: Optional[str] = None
