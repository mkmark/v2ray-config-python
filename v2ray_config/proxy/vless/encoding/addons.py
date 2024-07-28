from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class MultiLengthPacketWriter(Writer):
    pass


@dataclass(slots=True)
class LengthPacketWriter(Writer):
    cache: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class LengthPacketReader(Reader):
    cache: Optional[list[int]] = field(default_factory=list[int])
