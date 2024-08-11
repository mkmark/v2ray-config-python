from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.router as router
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.session as session
# import xray_config.common.strmatcher as strmatcher
# import xray_config.features as features
# import xray_config.features.dns as dns


@dataclass(slots=True)
class DNS(Mutex):
    tag: Optional[str] = None
    disableCache: Optional[bool] = None
    disableFallback: Optional[bool] = None
    disableFallbackIfMatch: Optional[bool] = None
    ipOption: Optional[IPOption] = field(default_factory=IPOption)
    hosts: Optional[StaticHosts] = field(default_factory=StaticHosts)
    clients: Optional[list[Client]] = field(default_factory=list[Client])
    ctx: Optional[Context] = field(default_factory=Context)
    domainMatcher: Optional[IndexMatcher] = field(default_factory=IndexMatcher)
    matcherInfos: Optional[list[DomainMatcherInfo]] = field(default_factory=list[DomainMatcherInfo])


@dataclass(slots=True)
class DomainMatcherInfo:
    clientIdx: Optional[int] = None
    domainRuleIdx: Optional[int] = None
