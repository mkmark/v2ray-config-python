from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.infra.conf.router_strategy import HealthCheckSettings

# import xray_config.app.observatory as observatory
# import xray_config.app.observatory.burst as burst
# import xray_config.infra.conf.cfgcommon.duration as duration


@dataclass(slots=True)
class ObservatoryConfig:
    subjectSelector: Optional[list[str]] = field(default_factory=list[str])
    probeURL: Optional[str] = None
    probeInterval: Optional[str] = None
    enableConcurrency: Optional[bool] = None


@dataclass(slots=True)
class BurstObservatoryConfig:
    subjectSelector: Optional[list[str]] = field(default_factory=list[str])
    pingConfig: Optional[HealthCheckSettings] = field(
        default_factory=HealthCheckSettings
    )
