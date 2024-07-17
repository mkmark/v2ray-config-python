from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protocol.udp as udp
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class PacketAddrDispatcher:
    conn: Optional[PacketConn] = field(default_factory=PacketConn)
    callback: Optional[ResponseCallback] = field(default_factory=ResponseCallback)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class PacketAddrDispatcherCreator:
    ctx: Optional[Context] = field(default_factory=Context)
