from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.transport.internet.request as request


@dataclass(slots=True)
class simpleAssemblerClient:
    assembly: Optional[TransportClientAssembly] = field(default_factory=TransportClientAssembly)
    config: Optional[ClientConfig] = field(default_factory=ClientConfig)


@dataclass(slots=True)
class simpleAssemblerClientSession:
    session_id: Optional[list[int]] = field(default_factory=list[int])
    current_write_wait: Optional[int] = None
    assembler: Optional[simpleAssemblerClient] = field(default_factory=simpleAssemblerClient)
    tripper: Optional[Tripper] = field(default_factory=Tripper)
    read_buffer: Optional[Buffer] = field(default_factory=Buffer)
    writer_chan: Optional[chan] = field(default_factory=chan)
    reader_chan: Optional[chan] = field(default_factory=chan)
    ctx: Optional[Context] = field(default_factory=Context)
