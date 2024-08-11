from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.net as net
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class sysConn:
    conn: Optional[UDPConn] = field(default_factory=UDPConn)
    header: Optional[PacketHeader] = field(default_factory=PacketHeader)
    auth: Optional[AEAD] = field(default_factory=AEAD)


@dataclass(slots=True)
class interConn:
    stream: Optional[Stream] = field(default_factory=Stream)
    local: Optional[Addr] = field(default_factory=Addr)
    remote: Optional[Addr] = field(default_factory=Addr)
