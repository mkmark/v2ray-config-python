from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.app.router.routercommon.common_pb import CIDR, Domain, GeoIP, GeoSite

# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class DomainStrategy(int):
    pass


@dataclass(slots=True)
class RoutingRule_Tag:
    tag: Optional[str] = None


@dataclass(slots=True)
class RoutingRule_BalancingTag:
    balancing_tag: Optional[str] = None


@dataclass(slots=True)
class RoutingRule:
    # target_tag: Optional[isRoutingRule_TargetTag] = field(default_factory=isRoutingRule_TargetTag)
    tag: Optional[str] = None
    balancing_tag: Optional[str] = None

    domain: Optional[list[Domain]] = field(default_factory=list[Domain])
    cidr: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    port_range: Optional[str] = None
    port_list: Optional[str] = None
    network_list: Optional[list[str]] = field(default_factory=list[str])
    networks: Optional[str] = None
    source_cidr: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    source_geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    source_port_list: Optional[str] = None
    user_email: Optional[list[str]] = field(default_factory=list[str])
    inbound_tag: Optional[list[str]] = field(default_factory=list[str])
    protocol: Optional[list[str]] = field(default_factory=list[str])
    attributes: Optional[str] = None
    domain_matcher: Optional[str] = None
    geo_domain: Optional[list[GeoSite]] = field(default_factory=list[GeoSite])


@dataclass(slots=True)
class BalancingRule:
    tag: Optional[str] = None
    outbound_selector: Optional[list[str]] = field(default_factory=list[str])
    strategy: Optional[str] = None
    strategy_settings: Optional[dict] = field(default_factory=dict)
    fallback_tag: Optional[str] = None


@dataclass(slots=True)
class StrategyWeight:
    regexp: Optional[bool] = None
    match: Optional[str] = None
    value: Optional[float] = None


@dataclass(slots=True)
class StrategyRandomConfig:
    observer_tag: Optional[str] = None
    alive_only: Optional[bool] = None


@dataclass(slots=True)
class StrategyLeastPingConfig:
    observer_tag: Optional[str] = None


@dataclass(slots=True)
class StrategyLeastLoadConfig:
    costs: Optional[list[StrategyWeight]] = field(default_factory=list[StrategyWeight])
    baselines: Optional[list[int]] = field(default_factory=list[int])
    expected: Optional[int] = None
    max_rtt: Optional[int] = None
    tolerance: Optional[float] = None
    observer_tag: Optional[str] = None


@dataclass(slots=True)
class Config:
    domain_strategy: Optional[str] = None
    rule: Optional[list[RoutingRule]] = field(default_factory=list[RoutingRule])
    balancing_rule: Optional[list[BalancingRule]] = field(
        default_factory=list[BalancingRule]
    )


@dataclass(slots=True)
class SimplifiedRoutingRule_Tag:
    tag: Optional[str] = None


@dataclass(slots=True)
class SimplifiedRoutingRule_BalancingTag:
    balancing_tag: Optional[str] = None


@dataclass(slots=True)
class SimplifiedRoutingRule:
    # target_tag: Optional[isSimplifiedRoutingRule_TargetTag] = field(default_factory=isSimplifiedRoutingRule_TargetTag)
    tag: Optional[str] = None
    balancing_tag: Optional[str] = None

    domain: Optional[list[Domain]] = field(default_factory=list[Domain])
    geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    port_list: Optional[str] = None
    networks: Optional[list[str]] = field(default_factory=list[str])
    source_geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    source_port_list: Optional[str] = None
    user_email: Optional[list[str]] = field(default_factory=list[str])
    inbound_tag: Optional[list[str]] = field(default_factory=list[str])
    protocol: Optional[list[str]] = field(default_factory=list[str])
    attributes: Optional[str] = None
    domain_matcher: Optional[str] = None
    geo_domain: Optional[list[GeoSite]] = field(default_factory=list[GeoSite])


@dataclass(slots=True)
class SimplifiedConfig:
    domain_strategy: Optional[DomainStrategy] = field(default_factory=DomainStrategy)
    rule: Optional[list[SimplifiedRoutingRule]] = field(
        default_factory=list[SimplifiedRoutingRule]
    )
    balancing_rule: Optional[list[BalancingRule]] = field(
        default_factory=list[BalancingRule]
    )


@dataclass(slots=True)
class x:
    pass
