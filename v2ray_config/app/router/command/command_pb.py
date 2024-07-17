from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.net as net
# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class RoutingContext:
    inbound_tag: Optional[str] = None
    network: Optional[str] = None
    source_i_ps: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    target_i_ps: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    source_port: Optional[int] = None
    target_port: Optional[int] = None
    target_domain: Optional[str] = None
    protocol: Optional[str] = None
    user: Optional[str] = None
    attributes: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    outbound_group_tags: Optional[list[str]] = field(default_factory=list[str])
    outbound_tag: Optional[str] = None


@dataclass(slots=True)
class SubscribeRoutingStatsRequest:
    field_selectors: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class TestRouteRequest:
    routing_context: Optional[RoutingContext] = field(default_factory=RoutingContext)
    field_selectors: Optional[list[str]] = field(default_factory=list[str])
    publish_result: Optional[bool] = None


@dataclass(slots=True)
class PrincipleTargetInfo:
    tag: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class OverrideInfo:
    target: Optional[str] = None


@dataclass(slots=True)
class BalancerMsg:
    override: Optional[OverrideInfo] = field(default_factory=OverrideInfo)
    principle_target: Optional[PrincipleTargetInfo] = field(default_factory=PrincipleTargetInfo)


@dataclass(slots=True)
class GetBalancerInfoRequest:
    tag: Optional[str] = None


@dataclass(slots=True)
class GetBalancerInfoResponse:
    balancer: Optional[BalancerMsg] = field(default_factory=BalancerMsg)


@dataclass(slots=True)
class OverrideBalancerTargetRequest:
    balancer_tag: Optional[str] = None
    target: Optional[str] = None


@dataclass(slots=True)
class OverrideBalancerTargetResponse:
    pass


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
