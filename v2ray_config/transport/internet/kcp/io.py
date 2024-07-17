from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class KCPPacketReader:
    security: Optional[AEAD] = field(default_factory=AEAD)
    header: Optional[PacketHeader] = field(default_factory=PacketHeader)


@dataclass(slots=True)
class KCPPacketWriter:
    header: Optional[PacketHeader] = field(default_factory=PacketHeader)
    security: Optional[AEAD] = field(default_factory=AEAD)
    writer: Optional[Writer] = field(default_factory=Writer)
