from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.platform as platform
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session


@dataclass(slots=True)
class PacketWriter:
    writer: Optional[Writer] = field(default_factory=Writer)
    dest: Optional[Destination] = field(default_factory=Destination)
    globalID: Optional[[8]byte] = field(default_factory=[8]byte)


@dataclass(slots=True)
class PacketReader:
    reader: Optional[Reader] = field(default_factory=Reader)
    cache: Optional[list[int]] = field(default_factory=list[int])
