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
    countAll: Optional[int] = None
    countFail: Optional[int] = None
    rTTAverage: Optional[str] = None
    rTTDeviation: Optional[str] = None
    rTTDeviationCost: Optional[str] = None
