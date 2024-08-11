from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.protocol as protocol
# import xray_config.proxy as proxy
# import xray_config.proxy.vless as vless


@dataclass(slots=True)
class MultiLengthPacketWriter(Writer):
    pass


@dataclass(slots=True)
class LengthPacketWriter(Writer):
    cache: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class LengthPacketReader(Reader):
    cache: Optional[list[int]] = field(default_factory=list[int])
