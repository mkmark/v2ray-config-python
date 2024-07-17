from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol.dns as dns
# import v2ray_config.common.protocol.udp as udp
# import v2ray_config.common.session as session
# import v2ray_config.common.signal.pubsub as pubsub
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.features.routing as routing
# import v2ray_config.transport.internet.udp as udp


@dataclass(slots=True)
class ClassicNameServer(RWMutex):
    name: Optional[str] = None
    address: Optional[Destination] = field(default_factory=Destination)
    ips: Optional[dict[str, record]] = field(default_factory=dict[str, record])
    requests: Optional[dict[int, dnsRequest]] = field(default_factory=dict[int, dnsRequest])
    pub: Optional[Service] = field(default_factory=Service)
    udp_server: Optional[DispatcherI] = field(default_factory=DispatcherI)
    cleanup: Optional[Periodic] = field(default_factory=Periodic)
    req_id: Optional[int] = None
