from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.features.outbound as outbound
# import xray_config.features.routing as routing


@dataclass(slots=True)
class Rule:
    tag: Optional[str] = None
    ruleTag: Optional[str] = None
    balancer: Optional[Balancer] = field(default_factory=Balancer)
    condition: Optional[Condition] = field(default_factory=Condition)
