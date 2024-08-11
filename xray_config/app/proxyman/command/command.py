from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.core as core
# import xray_config.features.inbound as inbound
# import xray_config.features.outbound as outbound
# import xray_config.proxy as proxy


@dataclass(slots=True)
class handlerServer:
    s: Optional[Instance] = field(default_factory=Instance)
    ihm: Optional[Manager] = field(default_factory=Manager)
    ohm: Optional[Manager] = field(default_factory=Manager)


@dataclass(slots=True)
class service:
    v: Optional[Instance] = field(default_factory=Instance)
