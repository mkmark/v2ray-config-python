from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.environment as environment
# import v2ray_config.common.environment.envctx as envctx
# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.udp as udp


# @dataclass(slots=True)
# class Handler:
#     ctx: Optional[Context] = field(default_factory=Context)


# @dataclass(slots=True)
# class status:
#     ctx: Optional[Context] = field(default_factory=Context)
#     password: Optional[list[int]] = field(default_factory=list[int])
#     msgbus: Optional[Bus] = field(default_factory=Bus)
#     udpdialer: Optional[UnderlayTransportDialer] = field(default_factory=UnderlayTransportDialer)
#     puni: Optional[PacketUniClient] = field(default_factory=PacketUniClient)
#     udprelay: Optional[PacketSCTPRelay] = field(default_factory=PacketSCTPRelay)
#     udpserver: Optional[UDPClientContext] = field(default_factory=UDPClientContext)
#     tunnel_tx_to_tun: Optional[chan] = field(default_factory=chan)
#     tunnel_rx_from_tun: Optional[chan] = field(default_factory=chan)
#     conn_adp: Optional[UDPConn2Tun] = field(default_factory=UDPConn2Tun)
#     config: Optional[UDPProtocolConfig] = field(default_factory=UDPProtocolConfig)
#     access: Optional[Mutex] = field(default_factory=Mutex)
