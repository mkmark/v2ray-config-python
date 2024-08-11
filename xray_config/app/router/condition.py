from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.strmatcher as strmatcher
# import xray_config.features.routing as routing


@dataclass(slots=True)
class ConditionChan(list[Condition]):
    pass


@dataclass(slots=True)
class DomainMatcher:
    matchers: Optional[IndexMatcher] = field(default_factory=IndexMatcher)


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
    configuredKeys: Optional[dict[str, Regexp]] = field(default_factory=dict[str, Regexp])
