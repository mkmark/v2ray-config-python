from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router as router
# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net
# import v2ray_config.infra.conf.cfgcommon as cfgcommon


@dataclass(slots=True)
class RouterRule:
    type: Optional[str] = None
    outbound_tag: Optional[str] = None
    balancer_tag: Optional[str] = None
    domain_matcher: Optional[str] = None


@dataclass(slots=True)
class RawFieldRule(RouterRule):
    domain: Optional[list[str]] = field(default_factory=list[str])
    domains: Optional[list[str]] = field(default_factory=list[str])
    ip: Optional[list[str]] = field(default_factory=list[str])
    port: Optional[str | int] = None
    network: Optional[str] = None
    source: Optional[list[str]] = field(default_factory=list[str])
    source_port: Optional[list[str]] = field(default_factory=list[str])
    user: Optional[list[str]] = field(default_factory=list[str])
    inbound_tag: Optional[list[str]] = field(default_factory=list[str])
    protocol: Optional[list[str]] = field(default_factory=list[str])
    attrs: Optional[str] = None
