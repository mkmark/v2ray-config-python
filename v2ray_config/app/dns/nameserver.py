from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.dns.fakedns as fakedns
# import v2ray_config.app.router as router
# import v2ray_config.common.errors as errors
# import v2ray_config.common.net as net
# import v2ray_config.common.session as session
# import v2ray_config.features as features
# import v2ray_config.features.dns as dns
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class Client:
    server: Optional[Server] = field(default_factory=Server)
    client_ip: Optional[IP] = field(default_factory=IP)
    tag: Optional[str] = None
    query_strategy: Optional[IPOption] = field(default_factory=IPOption)
    cache_strategy: Optional[CacheStrategy] = field(default_factory=CacheStrategy)
    fallback_strategy: Optional[FallbackStrategy] = field(default_factory=FallbackStrategy)
    domains: Optional[list[str]] = field(default_factory=list[str])
    expect_i_ps: Optional[list[GeoIPMatcher]] = field(default_factory=list[GeoIPMatcher])
    fake_dns: Optional[Server] = field(default_factory=Server)
