from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.buf as buf
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.outbound as outbound
# import xray_config.features.policy as policy
# import xray_config.features.routing as routing
# import xray_config.features.routing.session as session
# import xray_config.features.stats as stats
# import xray_config.transport as transport
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class cachedReader(Mutex):
    reader: Optional[Reader] = field(default_factory=Reader)
    cache: Optional[MultiBuffer] = field(default_factory=MultiBuffer)


@dataclass(slots=True)
class DefaultDispatcher:
    ohm: Optional[Manager] = field(default_factory=Manager)
    router: Optional[Router] = field(default_factory=Router)
    policy: Optional[Manager] = field(default_factory=Manager)
    stats: Optional[Manager] = field(default_factory=Manager)
    dns: Optional[Client] = field(default_factory=Client)
    fdns: Optional[FakeDNSEngine] = field(default_factory=FakeDNSEngine)
