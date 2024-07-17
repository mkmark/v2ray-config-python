from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.transport.internet.request as request


@dataclass(slots=True)
class simpleAssemblerServer:
    sessions: Optional[Map] = field(default_factory=Map)
    assembly: Optional[TransportServerAssembly] = field(default_factory=TransportServerAssembly)


@dataclass(slots=True)
class simpleAssemblerServerSession:
    max_write_size: Optional[int] = None
    read_buffer: Optional[Buffer] = field(default_factory=Buffer)
    read_chan: Optional[chan] = field(default_factory=chan)
    request_processed: Optional[chan] = field(default_factory=chan)
    write_lock: Optional[Mutex] = field(default_factory=Mutex)
    write_buffer: Optional[Buffer] = field(default_factory=Buffer)
    ctx: Optional[Context] = field(default_factory=Context)
