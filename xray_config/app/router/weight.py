from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors


@dataclass(slots=True)
class weightScaler(func(value, weight float64) float64):
    pass


@dataclass(slots=True)
class WeightManager:
    settings: Optional[list[StrategyWeight]] = field(default_factory=list[StrategyWeight])
    cache: Optional[dict[str, float]] = field(default_factory=dict[str, float])
    scaler: Optional[weightScaler] = field(default_factory=weightScaler)
    defaultWeight: Optional[float] = None
    mu: Optional[Mutex] = field(default_factory=Mutex)
