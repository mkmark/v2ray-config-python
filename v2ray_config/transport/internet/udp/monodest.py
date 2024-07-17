from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class MonoDestUDPConn(AbstractPacketConn):
    dest: Optional[Addr] = field(default_factory=Addr)
