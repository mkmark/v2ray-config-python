from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.router.routercommon as routercommon
# import v2ray_config.common.platform as platform


@dataclass(slots=True)
class GeoIPCache(dict[str, GeoIP]):
    pass


@dataclass(slots=True)
class GeoSiteCache(dict[str, GeoSite]):
    pass
