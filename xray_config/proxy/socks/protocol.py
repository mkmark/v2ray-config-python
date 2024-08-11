from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class ServerSession:
    config: Optional[ServerConfig] = field(default_factory=ServerConfig)
    address: Optional[str] = None
    port: Optional[int] = None
    localAddress: Optional[str] = None


@dataclass(slots=True)
class UDPReader:
    reader: Optional[Reader] = field(default_factory=Reader)


@dataclass(slots=True)
class UDPWriter:
    writer: Optional[Writer] = field(default_factory=Writer)
    request: Optional[RequestHeader] = field(default_factory=RequestHeader)
