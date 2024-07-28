from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.platform as platform
# import v2ray_config.features.dns as dns
# import v2ray_config.features.outbound as outbound
# import v2ray_config.features.routing as routing
# import v2ray_config.features.routing.dns as dns
# import v2ray_config.infra.conf.cfgcommon as cfgcommon
# import v2ray_config.infra.conf.geodata as geodata


@dataclass(slots=True)
class Router:
    domainStrategy: Optional[DomainStrategy] = field(default_factory=DomainStrategy)
    rules: Optional[list[Rule]] = field(default_factory=list[Rule])
    balancers: Optional[dict[str, Balancer]] = field(default_factory=dict[str, Balancer])
    dns: Optional[Client] = field(default_factory=Client)


@dataclass(slots=True)
class Route(Context):
    outboundGroupTags: Optional[list[str]] = field(default_factory=list[str])
    outboundTag: Optional[str] = None
