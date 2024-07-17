from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protoext as protoext
# import v2ray_config.proxy.shadowsocks as shadowsocks


# @dataclass(slots=True)
# class ServerConfig:
#     method: Optional[CipherTypeWrapper] = field(default_factory=CipherTypeWrapper)
#     password: Optional[str] = None
#     networks: Optional[list[str]] = field(default_factory=list[str])
#     packet_encoding: Optional[PacketAddrType] = field(default_factory=PacketAddrType)


# @dataclass(slots=True)
# class ClientConfig:
#     address: Optional[str] = None
#     port: Optional[int] = None
#     method: Optional[CipherTypeWrapper] = field(default_factory=CipherTypeWrapper)
#     password: Optional[str] = None
#     experiment_reduced_iv_head_entropy: Optional[bool] = None


# @dataclass(slots=True)
# class CipherTypeWrapper:
#     value: Optional[CipherType] = field(default_factory=CipherType)


# @dataclass(slots=True)
# class x:
#     pass
