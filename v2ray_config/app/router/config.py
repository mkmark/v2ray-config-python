from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net
# import v2ray_config.common.serial as serial
# import v2ray_config.features.outbound as outbound
# import v2ray_config.features.routing as routing
# import v2ray_config.infra.conf.v5cfg as v5cfg


@dataclass(slots=True)
class Rule:
    tag: Optional[str] = None
    balancer: Optional[Balancer] = field(default_factory=Balancer)
    condition: Optional[Condition] = field(default_factory=Condition)


@dataclass(slots=True)
class BalancingRuleStub:
    tag: Optional[str] = None
    outbound_selector: Optional[list[str]] = field(default_factory=list[str])
    strategy: Optional[str] = None
    strategy_settings: Optional[dict] = field(default_factory=dict)
    fallback_tag: Optional[str] = None
