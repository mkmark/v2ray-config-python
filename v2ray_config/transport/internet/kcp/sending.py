from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class SendingWindow:
    cache: Optional[List] = field(default_factory=List)
    totalInFlightSize: Optional[int] = None
    writer: Optional[SegmentWriter] = field(default_factory=SegmentWriter)


@dataclass(slots=True)
class SendingWorker(RWMutex):
    conn: Optional[Connection] = field(default_factory=Connection)
    window: Optional[SendingWindow] = field(default_factory=SendingWindow)
    firstUnacknowledged: Optional[int] = None
    nextNumber: Optional[int] = None
    remoteNextNumber: Optional[int] = None
    controlWindow: Optional[int] = None
    fastResend: Optional[int] = None
    windowSize: Optional[int] = None
    firstUnacknowledgedUpdated: Optional[bool] = None
    closed: Optional[bool] = None
