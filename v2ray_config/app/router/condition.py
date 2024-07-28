from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net
# import v2ray_config.common.strmatcher as strmatcher
# import v2ray_config.features.routing as routing


@dataclass(slots=True)
class ConditionChan(list[Condition]):
    pass


@dataclass(slots=True)
class DomainMatcher:
    matcher: Optional[IndexMatcher] = field(default_factory=IndexMatcher)


@dataclass(slots=True)
class MultiGeoIPMatcher:
    matchers: Optional[list[GeoIPMatcher]] = field(default_factory=list[GeoIPMatcher])
    onSource: Optional[bool] = None


@dataclass(slots=True)
class PortMatcher:
    port: Optional[MemoryPortList] = field(default_factory=MemoryPortList)
    onSource: Optional[bool] = None


@dataclass(slots=True)
class NetworkMatcher:
    list: Optional[[8]bool] = field(default_factory=[8]bool)


@dataclass(slots=True)
class UserMatcher:
    user: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class InboundTagMatcher:
    tags: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class ProtocolMatcher:
    protocols: Optional[list[str]] = field(default_factory=list[str])


@dataclass(slots=True)
class AttributeMatcher:
    program: Optional[Program] = field(default_factory=Program)
