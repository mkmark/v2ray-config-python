from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.common.serial as serial


@dataclass(slots=True)
class Domain_Type(int):
    pass


@dataclass(slots=True)
class Config_DomainStrategy(int):
    pass


@dataclass(slots=True)
class Domain:
    type: Optional[Domain_Type] = field(default_factory=Domain_Type)
    value: Optional[str] = None
    # attribute: Optional[list[Domain_Attribute]] = field(default_factory=list[Domain_Attribute])


@dataclass(slots=True)
class CIDR:
    ip: Optional[list[int]] = field(default_factory=list[int])
    prefix: Optional[int] = None


@dataclass(slots=True)
class GeoIP:
    country_code: Optional[str] = None
    cidr: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    reverse_match: Optional[bool] = None


@dataclass(slots=True)
class GeoIPList:
    entry: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])


@dataclass(slots=True)
class GeoSite:
    country_code: Optional[str] = None
    domain: Optional[list[Domain]] = field(default_factory=list[Domain])


@dataclass(slots=True)
class GeoSiteList:
    entry: Optional[list[GeoSite]] = field(default_factory=list[GeoSite])


@dataclass(slots=True)
class RoutingRule:
    tag: Optional[str] = None
    balancingTag: Optional[str] = None

    # targetTag: Optional[isRoutingRule_TargetTag] = field(default_factory=isRoutingRule_TargetTag)
    rule_tag: Optional[str] = None
    domain: Optional[list[Domain]] = field(default_factory=list[Domain])
    cidr: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    port_range: Optional[str] = None
    port_list: Optional[list[str]] = field(default_factory=list[str])
    network_list: Optional[list[str]] = field(default_factory=list[str])
    networks: Optional[list[str]] = field(default_factory=list[str])
    source_cidr: Optional[list[CIDR]] = field(default_factory=list[CIDR])
    source_geoip: Optional[list[GeoIP]] = field(default_factory=list[GeoIP])
    source_port_list: Optional[list[str]] = field(default_factory=list[str])
    user_email: Optional[list[str]] = field(default_factory=list[str])
    inbound_tag: Optional[list[str]] = field(default_factory=list[str])
    protocol: Optional[list[str]] = field(default_factory=list[str])
    attributes: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    domain_matcher: Optional[str] = None


@dataclass(slots=True)
class RoutingRule_Tag:
    tag: Optional[str] = None


@dataclass(slots=True)
class RoutingRule_BalancingTag:
    balancingTag: Optional[str] = None


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
class StrategyLeastLoadConfig:
    costs: Optional[list[StrategyWeight]] = field(default_factory=list[StrategyWeight])
    baselines: Optional[list[int]] = field(default_factory=list[int])
    expected: Optional[int] = None
    maxRTT: Optional[int] = None
    tolerance: Optional[float] = None


@dataclass(slots=True)
class Config:
    domain_strategy: Optional[Config_DomainStrategy] = field(
        default_factory=Config_DomainStrategy
    )
    rule: Optional[list[RoutingRule]] = field(default_factory=list[RoutingRule])
    balancing_rule: Optional[list[BalancingRule]] = field(
        default_factory=list[BalancingRule]
    )


# @dataclass(slots=True)
# class Domain_Attribute:
#     key: Optional[str] = None
#     typedValue: Optional[isDomain_Attribute_TypedValue] = field(default_factory=isDomain_Attribute_TypedValue)


@dataclass(slots=True)
class Domain_Attribute_BoolValue:
    boolValue: Optional[bool] = None


@dataclass(slots=True)
class Domain_Attribute_IntValue:
    intValue: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
