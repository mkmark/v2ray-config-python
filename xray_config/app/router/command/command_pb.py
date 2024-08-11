from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net
# import xray_config.common.serial as serial


@dataclass(slots=True)
class RoutingContext:
    inboundTag: Optional[str] = None
    network: Optional[str] = None
    sourceIPs: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    targetIPs: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    sourcePort: Optional[int] = None
    targetPort: Optional[int] = None
    targetDomain: Optional[str] = None
    protocol: Optional[str] = None
    user: Optional[str] = None
    attributes: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    outboundGroupTags: Optional[list[str]] = field(default_factory=list[str])
    outboundTag: Optional[str] = None


@dataclass(slots=True)
class SubscribeRoutingStatsRequest:
    fieldSelectors: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class TestRouteRequest:
    routingContext: Optional[RoutingContext] = field(default_factory=RoutingContext)
    fieldSelectors: Optional[list[str]] = field(default_factory=list[str])
    publishResult: Optional[bool] = None


@dataclass(slots=True)
class PrincipleTargetInfo:
    tag: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class OverrideInfo:
    target: Optional[str] = None


@dataclass(slots=True)
class BalancerMsg:
    override: Optional[OverrideInfo] = field(default_factory=OverrideInfo)
    principle_target: Optional[PrincipleTargetInfo] = field(
        default_factory=PrincipleTargetInfo
    )


@dataclass(slots=True)
class GetBalancerInfoRequest:
    tag: Optional[str] = None


@dataclass(slots=True)
class GetBalancerInfoResponse:
    balancer: Optional[BalancerMsg] = field(default_factory=BalancerMsg)


@dataclass(slots=True)
class OverrideBalancerTargetRequest:
    balancerTag: Optional[str] = None
    target: Optional[str] = None


@dataclass(slots=True)
class OverrideBalancerTargetResponse:
    pass


@dataclass(slots=True)
class AddRuleRequest:
    config: Optional[dict] = field(default_factory=dict)
    shouldAppend: Optional[bool] = None


@dataclass(slots=True)
class AddRuleResponse:
    pass


@dataclass(slots=True)
class RemoveRuleRequest:
    ruleTag: Optional[str] = None


@dataclass(slots=True)
class RemoveRuleResponse:
    pass


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
