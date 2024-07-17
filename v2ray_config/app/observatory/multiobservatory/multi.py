from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.taggedfeatures as taggedfeatures
# import v2ray_config.features as features
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class Observer(TaggedFeatures):
    config: Optional[Config] = field(default_factory=Config)
    ctx: Optional[Context] = field(default_factory=Context)
