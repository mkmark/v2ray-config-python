from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class ReceivingWindow:
    cache: Optional[dict[int, DataSegment]] = field(default_factory=dict[int, DataSegment])


@dataclass(slots=True)
class AckList:
    writer: Optional[SegmentWriter] = field(default_factory=SegmentWriter)
    timestamps: Optional[list[int]] = field(default_factory=list[int])
    numbers: Optional[list[int]] = field(default_factory=list[int])
    nextFlush: Optional[list[int]] = field(default_factory=list[int])
    flushCandidates: Optional[list[int]] = field(default_factory=list[int])
    dirty: Optional[bool] = None


@dataclass(slots=True)
class ReceivingWorker(RWMutex):
    conn: Optional[Connection] = field(default_factory=Connection)
    leftOver: Optional[MultiBuffer] = field(default_factory=MultiBuffer)
    window: Optional[ReceivingWindow] = field(default_factory=ReceivingWindow)
    acklist: Optional[AckList] = field(default_factory=AckList)
    nextNumber: Optional[int] = None
    windowSize: Optional[int] = None
