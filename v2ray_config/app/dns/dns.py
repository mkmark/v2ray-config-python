from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.dns.fakedns as fakedns
# import v2ray_config.app.router as router
# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common as common
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.common.platform as platform
# import v2ray_config.common.session as session
# import v2ray_config.common.strmatcher as strmatcher
# import v2ray_config.features as features
# import v2ray_config.features.dns as dns
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.geodata as geodata


@dataclass(slots=True)
class DNS(Mutex):
    hosts: Optional[StaticHosts] = field(default_factory=StaticHosts)
    clients: Optional[list[Client]] = field(default_factory=list[Client])
    ctx: Optional[Context] = field(default_factory=Context)
    clientTags: Optional[dict[str, bool]] = field(default_factory=dict[str, bool])
    fakeDNSEngine: Optional[FakeDNSEngine] = field(default_factory=FakeDNSEngine)
    domainMatcher: Optional[IndexMatcher] = field(default_factory=IndexMatcher)
    matcherInfos: Optional[list[DomainMatcherInfo]] = field(default_factory=list[DomainMatcherInfo])


@dataclass(slots=True)
class DomainMatcherInfo:
    clientIdx: Optional[int] = None
    domainRuleIdx: Optional[int] = None
