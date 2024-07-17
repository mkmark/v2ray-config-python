from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.environment as environment
# import v2ray_config.common.environment.systemnetworkimpl as systemnetworkimpl
# import v2ray_config.common.environment.transientstorageimpl as transientstorageimpl
# import v2ray_config.common.serial as serial
# import v2ray_config.features as features
# import v2ray_config.features.dns as dns
# import v2ray_config.features.dns.localdns as localdns
# import v2ray_config.features.inbound as inbound
# import v2ray_config.features.outbound as outbound
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing
# import v2ray_config.features.stats as stats


@dataclass(slots=True)
class resolution:
    deps: Optional[list[Type]] = field(default_factory=list[Type])
    callback: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class Instance:
    access: Optional[Mutex] = field(default_factory=Mutex)
    features: Optional[list[Feature]] = field(default_factory=list[Feature])
    feature_resolutions: Optional[list[resolution]] = field(default_factory=list[resolution])
    running: Optional[bool] = None
    env: Optional[RootEnvironment] = field(default_factory=RootEnvironment)
    ctx: Optional[Context] = field(default_factory=Context)
