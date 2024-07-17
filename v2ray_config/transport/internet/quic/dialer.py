from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.task as task
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class connectionContext:
    raw_conn: Optional[sysConn] = field(default_factory=sysConn)
    conn: Optional[Connection] = field(default_factory=Connection)


@dataclass(slots=True)
class clientConnections:
    access: Optional[Mutex] = field(default_factory=Mutex)
    conns: Optional[dict[Destination][, connectionContext]] = field(default_factory=dict[Destination][, connectionContext])
    cleanup: Optional[Periodic] = field(default_factory=Periodic)
