from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.net as net


@dataclass(slots=True)
class GeoIPMatcher:
    countryCode: Optional[str] = None
    reverseMatch: Optional[bool] = None
    ip4: Optional[IPSet] = field(default_factory=IPSet)
    ip6: Optional[IPSet] = field(default_factory=IPSet)


@dataclass(slots=True)
class GeoIPMatcherContainer:
    matchers: Optional[list[GeoIPMatcher]] = field(default_factory=list[GeoIPMatcher])
