from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class SendingWindow:
    cache: Optional[List] = field(default_factory=List)
    total_in_flight_size: Optional[int] = None
    writer: Optional[SegmentWriter] = field(default_factory=SegmentWriter)


@dataclass(slots=True)
class SendingWorker(RWMutex):
    conn: Optional[Connection] = field(default_factory=Connection)
    window: Optional[SendingWindow] = field(default_factory=SendingWindow)
    first_unacknowledged: Optional[int] = None
    next_number: Optional[int] = None
    remote_next_number: Optional[int] = None
    control_window: Optional[int] = None
    fast_resend: Optional[int] = None
    window_size: Optional[int] = None
    first_unacknowledged_updated: Optional[bool] = None
    closed: Optional[bool] = None
