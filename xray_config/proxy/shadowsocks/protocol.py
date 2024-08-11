from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.crypto as crypto
# import xray_config.common.drain as drain
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class FullReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    buffer: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class UDPReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    user: Optional[MemoryUser] = field(default_factory=MemoryUser)


@dataclass(slots=True)
class UDPWriter:
    writer: Optional[Writer] = field(default_factory=Writer)
    request: Optional[RequestHeader] = field(default_factory=RequestHeader)
