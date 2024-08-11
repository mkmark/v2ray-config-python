from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# from xray_config.app.router.condition import AttributeMatcher

# import xray_config.app.router as router
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.platform.filesystem as filesystem
# import xray_config.common.serial as serial


@dataclass(slots=True)
class BooleanMatcher(str):
    pass


@dataclass(slots=True)
class RouterRulesConfig:
    rules: Optional[list[dict]] = field(default_factory=list[dict])
    domainStrategy: Optional[str] = None


@dataclass(slots=True)
class StrategyConfig:
    type: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class BalancingRule:
    tag: Optional[str] = None
    selector: Optional[list[str]] = field(default_factory=list[str])
    strategy: Optional[StrategyConfig] = field(default_factory=StrategyConfig)
    fallbackTag: Optional[str] = None


@dataclass(slots=True)
class RouterRule:
    ruleTag: Optional[str] = None
    type: Optional[str] = None
    outboundTag: Optional[str] = None
    balancerTag: Optional[str] = None
    domainMatcher: Optional[str] = None


# @dataclass(slots=True)
# class AttributeList:
#     matcher: Optional[list[AttributeMatcher]] = field(
#         default_factory=list[AttributeMatcher]
#     )


@dataclass(slots=True)
class RawFieldRule(RouterRule):
    domain: Optional[list[str]] = field(default_factory=list[str])
    domains: Optional[list[str]] = field(default_factory=list[str])
    ip: Optional[list[str]] = field(default_factory=list[str])
    port: Optional[str | int] = None
    network: Optional[str] = None
    source: Optional[list[str]] = field(default_factory=list[str])
    sourcePort: Optional[list[str]] = field(default_factory=list[str])
    user: Optional[list[str]] = field(default_factory=list[str])
    inboundTag: Optional[list[str]] = field(default_factory=list[str])
    protocol: Optional[list[str]] = field(default_factory=list[str])
    attrs: Optional[dict[str, str]] = field(default_factory=dict[str, str])


@dataclass(slots=True)
class RouterConfig:
    settings: Optional[RouterRulesConfig] = field(default_factory=RouterRulesConfig)
    rules: Optional[list[RawFieldRule]] = field(default_factory=list[RawFieldRule])
    domainStrategy: Optional[str] = None
    balancers: Optional[list[BalancingRule]] = field(
        default_factory=list[BalancingRule]
    )
    domainMatcher: Optional[str] = None
