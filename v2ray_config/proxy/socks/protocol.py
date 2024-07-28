from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol


@dataclass(slots=True)
class ServerSession:
    config: Optional[ServerConfig] = field(default_factory=ServerConfig)
    address: Optional[str] = None
    port: Optional[int] = None
    clientAddress: Optional[str] = None


@dataclass(slots=True)
class UDPReader:
    reader: Optional[Reader] = field(default_factory=Reader)


@dataclass(slots=True)
class UDPWriter:
    request: Optional[RequestHeader] = field(default_factory=RequestHeader)
    writer: Optional[Writer] = field(default_factory=Writer)
