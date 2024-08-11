from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.net as net
# import xray_config.transport as transport


@dataclass(slots=True)
class PacketConnWrapper(Reader, Writer, Conn):
    dest: Optional[Destination] = field(default_factory=Destination)
    cached: Optional[MultiBuffer] = field(default_factory=MultiBuffer)
