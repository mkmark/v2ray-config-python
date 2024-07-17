from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.serial as serial
# import v2ray_config.features.inbound as inbound
# import v2ray_config.features.outbound as outbound
# import v2ray_config.proxy as proxy


@dataclass(slots=True)
class handlerServer:
    s: Optional[Instance] = field(default_factory=Instance)
    ihm: Optional[Manager] = field(default_factory=Manager)
    ohm: Optional[Manager] = field(default_factory=Manager)


@dataclass(slots=True)
class service:
    v: Optional[Instance] = field(default_factory=Instance)
