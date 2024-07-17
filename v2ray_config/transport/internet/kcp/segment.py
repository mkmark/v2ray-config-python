from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf


@dataclass(slots=True)
class Command(int):
    pass


@dataclass(slots=True)
class SegmentOption(int):
    pass


@dataclass(slots=True)
class DataSegment:
    conv: Optional[int] = None
    option: Optional[SegmentOption] = field(default_factory=SegmentOption)
    timestamp: Optional[int] = None
    number: Optional[int] = None
    sending_next: Optional[int] = None
    payload: Optional[Buffer] = field(default_factory=Buffer)
    timeout: Optional[int] = None
    transmit: Optional[int] = None


@dataclass(slots=True)
class AckSegment:
    conv: Optional[int] = None
    option: Optional[SegmentOption] = field(default_factory=SegmentOption)
    receiving_window: Optional[int] = None
    receiving_next: Optional[int] = None
    timestamp: Optional[int] = None
    number_list: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class CmdOnlySegment:
    conv: Optional[int] = None
    cmd: Optional[Command] = field(default_factory=Command)
    option: Optional[SegmentOption] = field(default_factory=SegmentOption)
    sending_next: Optional[int] = None
    receiving_next: Optional[int] = None
    peer_rto: Optional[int] = None
