from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.features.dns as dns
# import xray_config.features.outbound as outbound


@dataclass(slots=True)
class DefaultSystemDialer:
    controllers: Optional[list[Func]] = field(default_factory=list[Func])
    dns: Optional[Client] = field(default_factory=Client)
    obm: Optional[Manager] = field(default_factory=Manager)


@dataclass(slots=True)
class PacketConnWrapper:
    conn: Optional[PacketConn] = field(default_factory=PacketConn)
    dest: Optional[Addr] = field(default_factory=Addr)


@dataclass(slots=True)
class SimpleSystemDialer:
    adapter: Optional[SystemDialerAdapter] = field(default_factory=SystemDialerAdapter)
