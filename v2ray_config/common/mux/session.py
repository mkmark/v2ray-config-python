from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class SessionManager(RWMutex):
    sessions: Optional[dict[int, Session]] = field(default_factory=dict[int, Session])
    count: Optional[int] = None
    closed: Optional[bool] = None


@dataclass(slots=True)
class Session:
    input: Optional[Reader] = field(default_factory=Reader)
    output: Optional[Writer] = field(default_factory=Writer)
    parent: Optional[SessionManager] = field(default_factory=SessionManager)
    iD: Optional[int] = None
    transferType: Optional[TransferType] = field(default_factory=TransferType)
