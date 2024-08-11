from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from xray_config.app.router.config_pb import StrategyWeight

# import xray_config.app.router as router
# import xray_config.app.observatory.burst as burst
# import xray_config.infra.conf.cfgcommon.duration as duration


@dataclass(slots=True)
class StrategyEmptyConfig:
    pass


@dataclass(slots=True)
class StrategyLeastLoadConfig:
    costs: Optional[list[StrategyWeight]] = field(default_factory=list[StrategyWeight])
    baselines: Optional[list[str]] = field(default_factory=list[str])
    expected: Optional[int] = None
    maxRTT: Optional[str] = None
    tolerance: Optional[float] = None


@dataclass(slots=True)
class HealthCheckSettings:
    destination: Optional[str] = None
    connectivity: Optional[str] = None
    interval: Optional[str] = None
    sampling: Optional[int] = None
    timeout: Optional[str] = None
