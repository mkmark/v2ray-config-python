from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.transport.internet.transportcommon as transportcommon
# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet.request as request


@dataclass(slots=True)
class httpTripperClient:
    httpRTT: Optional[RoundTripper] = field(default_factory=RoundTripper)
    config: Optional[ClientConfig] = field(default_factory=ClientConfig)
    assembly: Optional[TransportClientAssembly] = field(default_factory=TransportClientAssembly)


@dataclass(slots=True)
class unimplementedBackDrop:
    pass


@dataclass(slots=True)
class httpTripperServer:
    ctx: Optional[Context] = field(default_factory=Context)
    listener: Optional[Listener] = field(default_factory=Listener)
    assembly: Optional[TransportServerAssembly] = field(default_factory=TransportServerAssembly)
    config: Optional[ServerConfig] = field(default_factory=ServerConfig)
