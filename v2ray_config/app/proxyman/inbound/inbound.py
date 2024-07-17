from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.proxyman as proxyman
# import v2ray_config.common as common
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.features.inbound as inbound


@dataclass(slots=True)
class Manager:
    ctx: Optional[Context] = field(default_factory=Context)
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    untagged_handler: Optional[list[Handler]] = field(default_factory=list[Handler])
    tagged_handlers: Optional[dict[str, Handler]] = field(default_factory=dict[str, Handler])
    running: Optional[bool] = None
