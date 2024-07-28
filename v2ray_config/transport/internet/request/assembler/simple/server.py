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
    maxWriteSize: Optional[int] = None
    readBuffer: Optional[Buffer] = field(default_factory=Buffer)
    readChan: Optional[chan] = field(default_factory=chan)
    requestProcessed: Optional[chan] = field(default_factory=chan)
    writeLock: Optional[Mutex] = field(default_factory=Mutex)
    writeBuffer: Optional[Buffer] = field(default_factory=Buffer)
    ctx: Optional[Context] = field(default_factory=Context)
