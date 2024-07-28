from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.infra.conf.rule.rule import RawFieldRule

# import v2ray_config.app.router as router
# import v2ray_config.common.platform as platform
# import v2ray_config.common.serial as serial
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.geodata as geodata
# import v2ray_config.infra.conf.rule as rule


@dataclass(slots=True)
class RouterRulesConfig:
    rules: Optional[list[dict]] = field(default_factory=list[dict])
    domainStrategy: Optional[str] = None


@dataclass(slots=True)
class StrategyConfig:
    type: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class BalancingRule:
    tag: Optional[str] = None
    selector: Optional[list[str]] = field(default_factory=list[str])
    strategy: Optional[StrategyConfig] = field(default_factory=StrategyConfig)
    fallbackTag: Optional[str] = None


@dataclass(slots=True)
class RouterConfig:
    settings: Optional[RouterRulesConfig] = field(default_factory=RouterRulesConfig)
    rules: Optional[list[RawFieldRule]] = field(default_factory=list[dict])
    domainStrategy: Optional[str] = None
    balancers: Optional[list[BalancingRule]] = field(
        default_factory=list[BalancingRule]
    )
    domainMatcher: Optional[str] = None
