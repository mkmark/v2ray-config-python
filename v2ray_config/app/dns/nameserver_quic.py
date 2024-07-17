from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.dns as dns
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.pubsub as pubsub
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.transport.internet.tls as tls


@dataclass(slots=True)
class QUICNameServer(RWMutex):
    ips: Optional[dict[str, record]] = field(default_factory=dict[str, record])
    pub: Optional[Service] = field(default_factory=Service)
    cleanup: Optional[Periodic] = field(default_factory=Periodic)
    req_id: Optional[int] = None
    name: Optional[str] = None
    destination: Optional[Destination] = field(default_factory=Destination)
    connection: Optional[Connection] = field(default_factory=Connection)
