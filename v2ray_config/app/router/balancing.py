from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.features.extension as extension
# import v2ray_config.features.outbound as outbound


@dataclass(slots=True)
class Balancer:
    selectors: Optional[list[str]] = field(default_factory=list[str])
    strategy: Optional[BalancingStrategy] = field(default_factory=BalancingStrategy)
    ohm: Optional[Manager] = field(default_factory=Manager)
    fallbackTag: Optional[str] = None
    override: Optional[override] = field(default_factory=override)
