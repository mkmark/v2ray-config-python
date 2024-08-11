from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.signal.done as done
# import xray_config.core as core
# import xray_config.features.extension as extension
# import xray_config.features.outbound as outbound


@dataclass(slots=True)
class Observer:
    config: Optional[Config] = field(default_factory=Config)
    ctx: Optional[Context] = field(default_factory=Context)
    statusLock: Optional[Mutex] = field(default_factory=Mutex)
    hp: Optional[HealthPing] = field(default_factory=HealthPing)
    finished: Optional[Instance] = field(default_factory=Instance)
    ohm: Optional[Manager] = field(default_factory=Manager)
