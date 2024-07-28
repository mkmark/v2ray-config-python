from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.common as common
# import v2ray_config.common.errors as errors
# import v2ray_config.common.session as session
# import v2ray_config.features.outbound as outbound


@dataclass(slots=True)
class Manager:
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    defaultHandler: Optional[Handler] = field(default_factory=Handler)
    taggedHandler: Optional[dict[str, Handler]] = field(default_factory=dict[str, Handler])
    untaggedHandlers: Optional[list[Handler]] = field(default_factory=list[Handler])
    running: Optional[bool] = None
