from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet.transportcommon as transportcommon
# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.request as request


@dataclass(slots=True)
class client:
    tripper: Optional[RoundTripperClient] = field(default_factory=RoundTripperClient)
    assembler: Optional[SessionAssemblerClient] = field(default_factory=SessionAssemblerClient)
    streamSettings: Optional[MemoryStreamConfig] = field(default_factory=MemoryStreamConfig)
    dest: Optional[Destination] = field(default_factory=Destination)


@dataclass(slots=True)
class clientConnection(Session):
    pass
