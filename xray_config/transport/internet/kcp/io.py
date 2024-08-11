from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class KCPPacketReader:
    security: Optional[AEAD] = field(default_factory=AEAD)
    header: Optional[PacketHeader] = field(default_factory=PacketHeader)


@dataclass(slots=True)
class KCPPacketWriter:
    header: Optional[PacketHeader] = field(default_factory=PacketHeader)
    security: Optional[AEAD] = field(default_factory=AEAD)
    writer: Optional[Writer] = field(default_factory=Writer)
