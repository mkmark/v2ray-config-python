from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.udp as udp
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class HubOption(func(h *Hub)):
    pass


@dataclass(slots=True)
class Hub:
    conn: Optional[UDPConn] = field(default_factory=UDPConn)
    cache: Optional[chan] = field(default_factory=chan)
    capacity: Optional[int] = None
    recvOrigDest: Optional[bool] = None
