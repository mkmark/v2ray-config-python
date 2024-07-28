from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet.transportcommon as transportcommon
# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.request as request


@dataclass(slots=True)
class server:
    tripper: Optional[RoundTripperServer] = field(default_factory=RoundTripperServer)
    assembler: Optional[SessionAssemblerServer] = field(default_factory=SessionAssemblerServer)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
    streamSettings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    addr: Optional[str] = None
    port: Optional[int] = None


@dataclass(slots=True)
class serverConnection(Session):
    pass
