from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.core as core
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Conn(Conn):
    pass


@dataclass(slots=True)
class UConn(UConn):
    serverName: Optional[str] = None
    authKey: Optional[list[int]] = field(default_factory=list[int])
    verified: Optional[bool] = None
