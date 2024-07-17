from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.dns.fakedns as fakedns
# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class DomainMatchingType(int):
    pass


@dataclass(slots=True)
class QueryStrategy(int):
    pass


@dataclass(slots=True)
class CacheStrategy(int):
    pass


@dataclass(slots=True)
class FallbackStrategy(int):
    pass


@dataclass(slots=True)
class NameServer:
    address: Optional[Endpoint] = field(default_factory=Endpoint)
    client_ip: Optional[list[int]] = field(default_factory=list[int])
    tag: Optional[str] = None
    prioritized_domain: Optional[list[NameServer_PriorityDomain]] = field(default_factory=list[NameServer_PriorityDomain])
    geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    original_rules: Optional[list[NameServer_OriginalRule]] = field(default_factory=list[NameServer_OriginalRule])
    fake_dns: Optional[FakeDnsPoolMulti] = field(default_factory=FakeDnsPoolMulti)
    skip_fallback: Optional[bool] = None
    query_strategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)
    cache_strategy: Optional[CacheStrategy] = field(default_factory=CacheStrategy)
    fallback_strategy: Optional[FallbackStrategy] = field(default_factory=FallbackStrategy)


@dataclass(slots=True)
class HostMapping:
    type: Optional[DomainMatchingType] = field(default_factory=DomainMatchingType)
    domain: Optional[str] = None
    ip: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    proxied_domain: Optional[str] = None


@dataclass(slots=True)
class Config:
    name_servers: Optional[list[Endpoint]] = field(default_factory=list[Endpoint])
    name_server: Optional[list[NameServer]] = field(default_factory=list[NameServer])
    hosts: Optional[dict[str, IPOrDomain]] = field(default_factory=dict[str, IPOrDomain])
    client_ip: Optional[list[int]] = field(default_factory=list[int])
    static_hosts: Optional[list[HostMapping]] = field(default_factory=list[HostMapping])
    fake_dns: Optional[FakeDnsPoolMulti] = field(default_factory=FakeDnsPoolMulti)
    tag: Optional[str] = None
    domain_matcher: Optional[str] = None
    disable_cache: Optional[bool] = None
    disable_fallback: Optional[bool] = None
    disable_fallback_if_match: Optional[bool] = None
    query_strategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)
    cache_strategy: Optional[CacheStrategy] = field(default_factory=CacheStrategy)
    fallback_strategy: Optional[FallbackStrategy] = field(default_factory=FallbackStrategy)


@dataclass(slots=True)
class SimplifiedConfig:
    name_server: Optional[list[SimplifiedNameServer]] = field(default_factory=list[SimplifiedNameServer])
    client_ip: Optional[str] = None
    static_hosts: Optional[list[SimplifiedHostMapping]] = field(default_factory=list[SimplifiedHostMapping])
    fake_dns: Optional[FakeDnsPoolMulti] = field(default_factory=FakeDnsPoolMulti)
    tag: Optional[str] = None
    domain_matcher: Optional[str] = None
    disable_cache: Optional[bool] = None
    disable_fallback: Optional[bool] = None
    disable_fallback_if_match: Optional[bool] = None
    query_strategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)
    cache_strategy: Optional[CacheStrategy] = field(default_factory=CacheStrategy)
    fallback_strategy: Optional[FallbackStrategy] = field(default_factory=FallbackStrategy)


@dataclass(slots=True)
class SimplifiedHostMapping:
    type: Optional[DomainMatchingType] = field(default_factory=DomainMatchingType)
    domain: Optional[str] = None
    ip: Optional[list[str]] = field(default_factory=list[str])
    proxied_domain: Optional[str] = None


@dataclass(slots=True)
class SimplifiedNameServer:
    address: Optional[Endpoint] = field(default_factory=Endpoint)
    client_ip: Optional[str] = None
    tag: Optional[str] = None
    prioritized_domain: Optional[list[SimplifiedNameServer_PriorityDomain]] = field(default_factory=list[SimplifiedNameServer_PriorityDomain])
    geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    original_rules: Optional[list[SimplifiedNameServer_OriginalRule]] = field(default_factory=list[SimplifiedNameServer_OriginalRule])
    fake_dns: Optional[FakeDnsPoolMulti] = field(default_factory=FakeDnsPoolMulti)
    skip_fallback: Optional[bool] = None
    query_strategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)
    cache_strategy: Optional[CacheStrategy] = field(default_factory=CacheStrategy)
    fallback_strategy: Optional[FallbackStrategy] = field(default_factory=FallbackStrategy)
    geo_domain: Optional[list[GeoSite]] = field(default_factory=list[GeoSite])


@dataclass(slots=True)
class NameServer_PriorityDomain:
    type: Optional[DomainMatchingType] = field(default_factory=DomainMatchingType)
    domain: Optional[str] = None


@dataclass(slots=True)
class NameServer_OriginalRule:
    rule: Optional[str] = None
    size: Optional[int] = None


@dataclass(slots=True)
class SimplifiedNameServer_PriorityDomain:
    type: Optional[DomainMatchingType] = field(default_factory=DomainMatchingType)
    domain: Optional[str] = None


@dataclass(slots=True)
class SimplifiedNameServer_OriginalRule:
    rule: Optional[str] = None
    size: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
