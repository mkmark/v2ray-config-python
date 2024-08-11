from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.router as router
# import xray_config.common.net as net


@dataclass(slots=True)
class DomainMatchingType(int):
    pass


@dataclass(slots=True)
class QueryStrategy(int):
    pass


@dataclass(slots=True)
class NameServer:
    address: Optional[Endpoint] = field(default_factory=Endpoint)
    client_ip: Optional[list[int]] = field(default_factory=list[int])
    skipFallback: Optional[bool] = None
    prioritized_domain: Optional[list[NameServer_PriorityDomain]] = field(default_factory=list[NameServer_PriorityDomain])
    geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    original_rules: Optional[list[NameServer_OriginalRule]] = field(default_factory=list[NameServer_OriginalRule])
    query_strategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)


@dataclass(slots=True)
class Config:
    nameServers: Optional[list[Endpoint]] = field(default_factory=list[Endpoint])
    name_server: Optional[list[NameServer]] = field(default_factory=list[NameServer])
    hosts: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    client_ip: Optional[list[int]] = field(default_factory=list[int])
    static_hosts: Optional[list[Config_HostMapping]] = field(default_factory=list[Config_HostMapping])
    tag: Optional[str] = None
    disableCache: Optional[bool] = None
    query_strategy: Optional[QueryStrategy] = field(default_factory=QueryStrategy)
    disableFallback: Optional[bool] = None
    disableFallbackIfMatch: Optional[bool] = None


@dataclass(slots=True)
class NameServer_PriorityDomain:
    type: Optional[DomainMatchingType] = field(default_factory=DomainMatchingType)
    domain: Optional[str] = None


@dataclass(slots=True)
class NameServer_OriginalRule:
    rule: Optional[str] = None
    size: Optional[int] = None


@dataclass(slots=True)
class Config_HostMapping:
    type: Optional[DomainMatchingType] = field(default_factory=DomainMatchingType)
    domain: Optional[str] = None
    ip: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    proxied_domain: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
