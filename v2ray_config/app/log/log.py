from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.log as log


@dataclass(slots=True)
class Instance(RWMutex):
    config: Optional[Config] = field(default_factory=Config)
    access_logger: Optional[Handler] = field(default_factory=Handler)
    error_logger: Optional[Handler] = field(default_factory=Handler)
    followers: Optional[dict[Value, func(msg]] = field(default_factory=dict[Value, func(msg])
    active: Optional[bool] = None
