from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.observatory as observatory
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.core as core
# import xray_config.features.extension as extension
# import xray_config.features.outbound as outbound


@dataclass(slots=True)
class RoundRobinStrategy:
    fallbackTag: Optional[str] = None
    ctx: Optional[Context] = field(default_factory=Context)
    observatory: Optional[Observatory] = field(default_factory=Observatory)
    mu: Optional[Mutex] = field(default_factory=Mutex)
    index: Optional[int] = None


@dataclass(slots=True)
class Balancer:
    selectors: Optional[list[str]] = field(default_factory=list[str])
    strategy: Optional[BalancingStrategy] = field(default_factory=BalancingStrategy)
    ohm: Optional[Manager] = field(default_factory=Manager)
    fallbackTag: Optional[str] = None
    override: Optional[override] = field(default_factory=override)
