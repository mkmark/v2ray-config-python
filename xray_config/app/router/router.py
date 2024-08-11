from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.serial as serial
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.outbound as outbound
# import xray_config.features.routing as routing
# import xray_config.features.routing.dns as dns


@dataclass(slots=True)
class Router:
    domainStrategy: Optional[Config_DomainStrategy] = field(default_factory=Config_DomainStrategy)
    rules: Optional[list[Rule]] = field(default_factory=list[Rule])
    balancers: Optional[dict[str, Balancer]] = field(default_factory=dict[str, Balancer])
    dns: Optional[Client] = field(default_factory=Client)
    ctx: Optional[Context] = field(default_factory=Context)
    ohm: Optional[Manager] = field(default_factory=Manager)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    mu: Optional[Mutex] = field(default_factory=Mutex)


@dataclass(slots=True)
class Route(Context):
    outboundGroupTags: Optional[list[str]] = field(default_factory=list[str])
    outboundTag: Optional[str] = None
