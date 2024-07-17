from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.app.router.config_pb import StrategyLeastPingConfig

# import v2ray_config.app.observatory as observatory
# import v2ray_config.common as common
# import v2ray_config.features as features
# import v2ray_config.features.extension as extension


@dataclass(slots=True)
class outboundList(list[str]):
    pass


@dataclass(slots=True)
class LeastPingStrategy:
    # ctx: Optional[Context] = field(default_factory=Context)
    # observatory: Optional[Observatory] = field(default_factory=Observatory)
    config: Optional[StrategyLeastPingConfig] = field(
        default_factory=StrategyLeastPingConfig
    )
