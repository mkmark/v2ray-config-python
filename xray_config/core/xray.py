from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.platform as platform
# import xray_config.common.serial as serial
# import xray_config.features as features
# import xray_config.features.dns as dns
# import xray_config.features.dns.localdns as localdns
# import xray_config.features.inbound as inbound
# import xray_config.features.outbound as outbound
# import xray_config.features.policy as policy
# import xray_config.features.routing as routing
# import xray_config.features.stats as stats
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class resolution:
    deps: Optional[list[Type]] = field(default_factory=list[Type])
    callback: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class Instance:
    access: Optional[Mutex] = field(default_factory=Mutex)
    features: Optional[list[Feature]] = field(default_factory=list[Feature])
    featureResolutions: Optional[list[resolution]] = field(default_factory=list[resolution])
    running: Optional[bool] = None
    ctx: Optional[Context] = field(default_factory=Context)
