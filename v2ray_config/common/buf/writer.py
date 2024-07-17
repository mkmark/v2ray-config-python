from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.errors as errors


@dataclass(slots=True)
class noOpWriter(int):
    pass


@dataclass(slots=True)
class BufferToBytesWriter(Writer):
    cache: Optional[list[list[int]]] = field(default_factory=list[list[int]])


@dataclass(slots=True)
class BufferedWriter(Mutex):
    writer: Optional[Writer] = field(default_factory=Writer)
    buffer: Optional[Buffer] = field(default_factory=Buffer)
    buffered: Optional[bool] = None


@dataclass(slots=True)
class SequentialWriter(Writer):
    pass
