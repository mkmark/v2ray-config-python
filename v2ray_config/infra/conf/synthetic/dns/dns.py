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
    clientIP: Optional[str] = None
    port: Optional[int] = None
    tag: Optional[str] = None
    queryStrategy: Optional[str] = None
    cacheStrategy: Optional[str] = None
    fallbackStrategy: Optional[str] = None
    skipFallback: Optional[bool] = None
    domains: Optional[list[str]] = field(default_factory=list[str])
    expectIPs: Optional[list[str]] = field(default_factory=list[str])
    fakeDNS: Optional[FakeDNSConfigExtend] = field(default_factory=FakeDNSConfigExtend)


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
    domainMatcher: Optional[str] = None
    clientIp: Optional[str] = None
    tag: Optional[str] = None
    queryStrategy: Optional[str] = None
    cacheStrategy: Optional[str] = None
    fallbackStrategy: Optional[str] = None
    disableCache: Optional[bool] = None
    disableFallback: Optional[bool] = None
    disableFallbackIfMatch: Optional[bool] = None
