from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.strmatcher as strmatcher
# import xray_config.features as features
# import xray_config.features.dns as dns


@dataclass(slots=True)
class StaticHosts:
    ips: Optional[list[list[str]]] = field(default_factory=list[list[str]])
    matchers: Optional[MatcherGroup] = field(default_factory=MatcherGroup)
