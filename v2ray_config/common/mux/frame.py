from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.bitmask as bitmask
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial


@dataclass(slots=True)
class SessionStatus(int):
    pass


@dataclass(slots=True)
class TargetNetwork(int):
    pass


@dataclass(slots=True)
class FrameMetadata:
    target: Optional[Destination] = field(default_factory=Destination)
    sessionID: Optional[int] = None
    option: Optional[Byte] = field(default_factory=Byte)
    sessionStatus: Optional[SessionStatus] = field(default_factory=SessionStatus)
