from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.infra.conf.synthetic.dns.fakedns import (
    FakeDNSConfig,
    FakeDNSConfigExtend,
)

# import v2ray_config.app.dns as dns
# import v2ray_config.app.dns.fakedns as fakedns
# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net
# import v2ray_config.common.platform as platform
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.geodata as geodata
# import v2ray_config.infra.conf.rule as rule


@dataclass(slots=True)
class NameServerConfig:
    address: Optional[str] = None
    client_ip: Optional[str] = None
    port: Optional[int] = None
    tag: Optional[str] = None
    query_strategy: Optional[str] = None
    cache_strategy: Optional[str] = None
    fallback_strategy: Optional[str] = None
    skip_fallback: Optional[bool] = None
    domains: Optional[list[str]] = field(default_factory=list[str])
    expect_i_ps: Optional[list[str]] = field(default_factory=list[str])
    fake_dns: Optional[FakeDNSConfigExtend] = field(default_factory=FakeDNSConfigExtend)


@dataclass(slots=True)
class HostAddress:
    addr: Optional[str] = None
    addrs: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class DNSConfig:
    servers: Optional[list[NameServerConfig]] = field(
        default_factory=list[NameServerConfig]
    )
    hosts: Optional[dict[str, HostAddress]] = field(
        default_factory=dict[str, HostAddress]
    )
    fakedns: Optional[FakeDNSConfig] = field(default_factory=FakeDNSConfig)
    domain_matcher: Optional[str] = None
    client_ip: Optional[str] = None
    tag: Optional[str] = None
    query_strategy: Optional[str] = None
    cache_strategy: Optional[str] = None
    fallback_strategy: Optional[str] = None
    disable_cache: Optional[bool] = None
    disable_fallback: Optional[bool] = None
    disable_fallback_if_match: Optional[bool] = None
