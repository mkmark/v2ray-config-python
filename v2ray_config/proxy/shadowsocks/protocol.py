from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.drain as drain
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class UDPReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    user: Optional[MemoryUser] = field(default_factory=MemoryUser)


@dataclass(slots=True)
class UDPWriter:
    writer: Optional[Writer] = field(default_factory=Writer)
    request: Optional[RequestHeader] = field(default_factory=RequestHeader)
