from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.infra.conf.geodata as geodata


@dataclass(slots=True)
class memConservativeLoader:
    geoipcache: Optional[GeoIPCache] = field(default_factory=GeoIPCache)
    geositecache: Optional[GeoSiteCache] = field(default_factory=GeoSiteCache)
