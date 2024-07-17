from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.observatory as observatory
# import v2ray_config.common as common
# import v2ray_config.common.dice as dice
# import v2ray_config.features as features
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class LeastLoadStrategy:
    settings: Optional[StrategyLeastLoadConfig] = field(default_factory=StrategyLeastLoadConfig)
    costs: Optional[WeightManager] = field(default_factory=WeightManager)
    observer: Optional[Observatory] = field(default_factory=Observatory)
    ctx: Optional[Context] = field(default_factory=Context)


@dataclass(slots=True)
class node:
    tag: Optional[str] = None
    count_all: Optional[int] = None
    count_fail: Optional[int] = None
    rtt_average: Optional[str] = None
    rtt_deviation: Optional[str] = None
    rtt_deviation_cost: Optional[str] = None
