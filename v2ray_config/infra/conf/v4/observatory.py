from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.infra.conf.synthetic.router.router_strategy import HealthCheckSettings

# import v2ray_config.app.observatory as observatory
# import v2ray_config.app.observatory.burst as burst
# import v2ray_config.app.observatory.multiobservatory as multiobservatory
# import v2ray_config.common.serial as serial
# import v2ray_config.common.taggedfeatures as taggedfeatures
# import v2ray_config.infra.conf.cfgcommon.duration as duration
# import v2ray_config.infra.conf.synthetic.router as router


@dataclass(slots=True)
class ObservatoryConfig:
    subjectSelector: Optional[list[str]] = field(default_factory=list[str])
    probeURL: Optional[str] = None
    probeInterval: Optional[str] = None


@dataclass(slots=True)
class BurstObservatoryConfig:
    subjectSelector: Optional[list[str]] = field(default_factory=list[str])
    pingConfig: Optional[HealthCheckSettings] = field(
        default_factory=HealthCheckSettings
    )


@dataclass(slots=True)
class MultiObservatoryItem:
    type: Optional[str] = None
    tag: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class MultiObservatoryConfig:
    observers: Optional[list[MultiObservatoryItem]] = field(
        default_factory=list[MultiObservatoryItem]
    )
