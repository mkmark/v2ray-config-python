from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.tun.packetparse as packetparse
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protocol.udp as udp
# import v2ray_config.features.routing as routing
# import v2ray_config.transport.internet.udp as udp


@dataclass(slots=True)
class TunSorter:
    tunWriter: Optional[Writer] = field(default_factory=Writer)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    packetAddrType: Optional[PacketAddrType] = field(default_factory=PacketAddrType)
    trackedConnections: Optional[Map] = field(default_factory=Map)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class trackedUDPConnection:
    packetDispatcher: Optional[DispatcherI] = field(default_factory=DispatcherI)
    tunSorter: Optional[TunSorter] = field(default_factory=TunSorter)
    src: Optional[Destination] = field(default_factory=Destination)
