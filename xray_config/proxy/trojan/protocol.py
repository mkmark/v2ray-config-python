from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class ConnWriter(Writer):
    target: Optional[Destination] = field(default_factory=Destination)
    account: Optional[MemoryAccount] = field(default_factory=MemoryAccount)
    headerSent: Optional[bool] = None


@dataclass(slots=True)
class PacketWriter(Writer):
    target: Optional[Destination] = field(default_factory=Destination)


@dataclass(slots=True)
class ConnReader(Reader):
    target: Optional[Destination] = field(default_factory=Destination)
    flow: Optional[str] = None
    headerParsed: Optional[bool] = None


@dataclass(slots=True)
class PacketReader(Reader):
    pass
