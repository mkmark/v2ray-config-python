from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.log as log
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.session as session
# import v2ray_config.common.strmatcher as strmatcher
# import v2ray_config.features.outbound as outbound
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing
# import v2ray_config.features.routing.session as session
# import v2ray_config.features.stats as stats
# import v2ray_config.transport as transport
# import v2ray_config.transport.pipe as pipe


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
