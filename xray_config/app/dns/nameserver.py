from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.router as router
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.strmatcher as strmatcher
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.routing as routing


@dataclass(slots=True)
class Client:
    server: Optional[Server] = field(default_factory=Server)
    clientIP: Optional[IP] = field(default_factory=IP)
    skipFallback: Optional[bool] = None
    domains: Optional[list[str]] = field(default_factory=list[str])
    expectIPs: Optional[list[GeoIPMatcher]] = field(default_factory=list[GeoIPMatcher])
