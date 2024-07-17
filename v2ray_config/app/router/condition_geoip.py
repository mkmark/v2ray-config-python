from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.net as net


@dataclass(slots=True)
class GeoIPMatcher:
    country_code: Optional[str] = None
    reverse_match: Optional[bool] = None
    ip_4: Optional[IPSet] = field(default_factory=IPSet)
    ip_6: Optional[IPSet] = field(default_factory=IPSet)


@dataclass(slots=True)
class GeoIPMatcherContainer:
    matchers: Optional[list[GeoIPMatcher]] = field(default_factory=list[GeoIPMatcher])
