from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.bitmask as bitmask
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.serial as serial


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
    globalID: Optional[[8]byte] = field(default_factory=[8]byte)
