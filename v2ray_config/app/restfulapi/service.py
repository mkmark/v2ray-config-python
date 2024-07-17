from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.features as features
# import v2ray_config.features.stats as stats


@dataclass(slots=True)
class restfulService:
    listener: Optional[Listener] = field(default_factory=Listener)
    config: Optional[Config] = field(default_factory=Config)
    access: Optional[Mutex] = field(default_factory=Mutex)
    stats: Optional[Manager] = field(default_factory=Manager)
    ctx: Optional[Context] = field(default_factory=Context)
