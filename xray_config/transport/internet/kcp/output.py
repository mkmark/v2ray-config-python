from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.retry as retry


@dataclass(slots=True)
class SimpleSegmentWriter(Mutex):
    buffer: Optional[Buffer] = field(default_factory=Buffer)
    writer: Optional[Writer] = field(default_factory=Writer)


@dataclass(slots=True)
class RetryableWriter:
    writer: Optional[SegmentWriter] = field(default_factory=SegmentWriter)
