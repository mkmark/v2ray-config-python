from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors


@dataclass(slots=True)
class uploadHeap(list[Packet]):
    pass


@dataclass(slots=True)
class Packet:
    payload: Optional[list[int]] = field(default_factory=list[int])
    seq: Optional[int] = None


@dataclass(slots=True)
class uploadQueue:
    pushedPackets: Optional[chan] = field(default_factory=chan)
    writeCloseMutex: Optional[Mutex] = field(default_factory=Mutex)
    heap: Optional[uploadHeap] = field(default_factory=uploadHeap)
    nextSeq: Optional[int] = None
    closed: Optional[bool] = None
    maxPackets: Optional[int] = None
