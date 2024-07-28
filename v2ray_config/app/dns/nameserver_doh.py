from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.dns as dns
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.pubsub as pubsub
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.features.routing as routing
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class DoHNameServer(RWMutex):
    ips: Optional[dict[str, record]] = field(default_factory=dict[str, record])
    pub: Optional[Service] = field(default_factory=Service)
    cleanup: Optional[Periodic] = field(default_factory=Periodic)
    reqID: Optional[int] = None
    httpClient: Optional[Client] = field(default_factory=Client)
    dohURL: Optional[str] = None
    name: Optional[str] = None
