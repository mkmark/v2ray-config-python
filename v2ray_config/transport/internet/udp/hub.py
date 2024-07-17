from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.udp as udp
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class HubOption(func(h *Hub)):
    pass


@dataclass(slots=True)
class Hub:
    conn: Optional[UDPConn] = field(default_factory=UDPConn)
    cache: Optional[chan] = field(default_factory=chan)
    capacity: Optional[int] = None
    recv_orig_dest: Optional[bool] = None
