from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protoext as protoext
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class Config:
    name: Optional[str] = None
    mtu: Optional[int] = None
    user_level: Optional[int] = None
    packet_encoding: Optional[PacketAddrType] = field(default_factory=PacketAddrType)
    tag: Optional[str] = None
    ips: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    routes: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    enable_promiscuous_mode: Optional[bool] = None
    enable_spoofing: Optional[bool] = None
    socket_settings: Optional[SocketConfig] = field(default_factory=SocketConfig)
    sniffing_settings: Optional[SniffingConfig] = field(default_factory=SniffingConfig)


@dataclass(slots=True)
class x:
    pass
