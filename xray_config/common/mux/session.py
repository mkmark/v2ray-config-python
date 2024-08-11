from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.transport.pipe as pipe


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
    closed: Optional[bool] = None
    xUDP: Optional[XUDP] = field(default_factory=XUDP)


@dataclass(slots=True)
class XUDP:
    globalID: Optional[[8]byte] = field(default_factory=[8]byte)
    status: Optional[int] = None
    expire: Optional[Time] = field(default_factory=Time)
    mux: Optional[Session] = field(default_factory=Session)
