from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.task as task
# import v2ray_config.features as features


@dataclass(slots=True)
class Holder:
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    features: Optional[dict[str, Feature]] = field(default_factory=dict[str, Feature])
    member_type: Optional[Type] = field(default_factory=Type)
    ctx: Optional[Context] = field(default_factory=Context)
