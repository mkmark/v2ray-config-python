from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.dice as dice
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.policy as policy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class Handler:
    conf: Optional[DeviceConfig] = field(default_factory=DeviceConfig)
    net: Optional[Tunnel] = field(default_factory=Tunnel)
    bind: Optional[netBindClient] = field(default_factory=netBindClient)
    policyManager: Optional[Manager] = field(default_factory=Manager)
    dns: Optional[Client] = field(default_factory=Client)
    endpoints: Optional[list[Addr]] = field(default_factory=list[Addr])
    hasIPv4,: Optional[hasIPv6] = field(default_factory=hasIPv6)
    wgLock: Optional[Mutex] = field(default_factory=Mutex)
