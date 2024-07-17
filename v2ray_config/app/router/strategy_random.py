from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.observatory as observatory
# import v2ray_config.common as common
# import v2ray_config.common.dice as dice
# import v2ray_config.features as features
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class RandomStrategy:
    ctx: Optional[Context] = field(default_factory=Context)
    settings: Optional[StrategyRandomConfig] = field(default_factory=StrategyRandomConfig)
    observatory: Optional[Observatory] = field(default_factory=Observatory)
