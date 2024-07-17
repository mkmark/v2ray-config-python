from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.session as session


@dataclass(slots=True)
class DefaultSystemDialer:
    controllers: Optional[list[controller]] = field(default_factory=list[controller])


@dataclass(slots=True)
class packetConnWrapper:
    conn: Optional[PacketConn] = field(default_factory=PacketConn)
    dest: Optional[Addr] = field(default_factory=Addr)


@dataclass(slots=True)
class SimpleSystemDialer:
    adapter: Optional[SystemDialerAdapter] = field(default_factory=SystemDialerAdapter)
