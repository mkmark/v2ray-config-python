from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol.dns as dns
# import xray_config.common.session as session
# import xray_config.common.signal.pubsub as pubsub
# import xray_config.common.task as task
# import xray_config.features.dns as dns
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class QUICNameServer(RWMutex):
    ips: Optional[dict[str, record]] = field(default_factory=dict[str, record])
    pub: Optional[Service] = field(default_factory=Service)
    cleanup: Optional[Periodic] = field(default_factory=Periodic)
    reqID: Optional[int] = None
    name: Optional[str] = None
    destination: Optional[Destination] = field(default_factory=Destination)
    connection: Optional[Connection] = field(default_factory=Connection)
    queryStrategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)
