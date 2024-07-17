from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.net as net
# import v2ray_config.common.strmatcher as strmatcher
# import v2ray_config.features as features
# import v2ray_config.features.dns as dns


@dataclass(slots=True)
class StaticHosts:
    ips: Optional[list[list[str]]] = field(default_factory=list[list[str]])
    matchers: Optional[LinearIndexMatcher] = field(default_factory=LinearIndexMatcher)
