from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.observatory as observatory
# import v2ray_config.common as common
# import v2ray_config.common.signal.done as done
# import v2ray_config.features.extension as extension
# import v2ray_config.features.outbound as outbound


@dataclass(slots=True)
class Observer:
    config: Optional[Config] = field(default_factory=Config)
    ctx: Optional[Context] = field(default_factory=Context)
    status_lock: Optional[Mutex] = field(default_factory=Mutex)
    hp: Optional[HealthPing] = field(default_factory=HealthPing)
    finished: Optional[Instance] = field(default_factory=Instance)
    ohm: Optional[Manager] = field(default_factory=Manager)
