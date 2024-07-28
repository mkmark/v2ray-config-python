from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

from v2ray_config.app.router.config_pb import StrategyWeight

# import v2ray_config.app.observatory.burst as burst
# import v2ray_config.app.router as router
# import v2ray_config.infra.conf.cfgcommon.duration as duration
# import v2ray_config.infra.conf.cfgcommon.loader as loader


@dataclass(slots=True)
class strategyEmptyConfig:
    pass


@dataclass(slots=True)
class strategyLeastLoadConfig:
    costs: Optional[list[StrategyWeight]] = field(default_factory=list[StrategyWeight])
    baselines: Optional[list[str]] = field(default_factory=list[str])
    expected: Optional[int] = None
    maxRTT: Optional[str] = None
    tolerance: Optional[float] = None
    observerTag: Optional[str] = None


@dataclass(slots=True)
class HealthCheckSettings:
    destination: Optional[str] = None
    connectivity: Optional[str] = None
    interval: Optional[str] = None
    sampling: Optional[int] = None
    timeout: Optional[str] = None


@dataclass(slots=True)
class strategyLeastPingConfig:
    observerTag: Optional[str] = None


@dataclass(slots=True)
class strategyRandomConfig:
    aliveOnly: Optional[bool] = None
    observerTag: Optional[str] = None
