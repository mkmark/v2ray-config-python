from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


# @dataclass(slots=True)
# class ConnWriter(Writer):
#     target: Optional[Destination] = field(default_factory=Destination)
#     account: Optional[MemoryAccount] = field(default_factory=MemoryAccount)
#     header_sent: Optional[bool] = None


# @dataclass(slots=True)
# class PacketWriter(Writer):
#     target: Optional[Destination] = field(default_factory=Destination)


# @dataclass(slots=True)
# class ConnReader(Reader):
#     target: Optional[Destination] = field(default_factory=Destination)
#     header_parsed: Optional[bool] = None


# @dataclass(slots=True)
# class PacketPayload:
#     target: Optional[Destination] = field(default_factory=Destination)
#     buffer: Optional[MultiBuffer] = field(default_factory=MultiBuffer)


# @dataclass(slots=True)
# class PacketReader(Reader):
#     pass


# @dataclass(slots=True)
# class PacketConnectionReader:
#     reader: Optional[PacketReader] = field(default_factory=PacketReader)
#     payload: Optional[PacketPayload] = field(default_factory=PacketPayload)
