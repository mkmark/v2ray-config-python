from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol.dns as dns
# import xray_config.common.protocol.udp as udp
# import xray_config.common.signal.pubsub as pubsub
# import xray_config.common.task as task
# import xray_config.features.dns as dns
# import xray_config.features.routing as routing
# import xray_config.transport.internet.udp as udp


@dataclass(slots=True)
class ClassicNameServer(RWMutex):
    name: Optional[str] = None
    address: Optional[Destination] = field(default_factory=Destination)
    ips: Optional[dict[str, record]] = field(default_factory=dict[str, record])
    requests: Optional[dict[int, dnsRequest]] = field(default_factory=dict[int, dnsRequest])
    pub: Optional[Service] = field(default_factory=Service)
    udpServer: Optional[Dispatcher] = field(default_factory=Dispatcher)
    cleanup: Optional[Periodic] = field(default_factory=Periodic)
    reqID: Optional[int] = None
