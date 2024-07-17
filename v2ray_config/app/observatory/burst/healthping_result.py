from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class HealthPingStats:
    all: Optional[int] = None
    fail: Optional[int] = None
    deviation: Optional[str] = None
    average: Optional[str] = None
    max: Optional[str] = None
    min: Optional[str] = None


@dataclass(slots=True)
class HealthPingRTTS:
    idx: Optional[int] = None
    cap: Optional[int] = None
    validity: Optional[str] = None
    rtts: Optional[list[pingRTT]] = field(default_factory=list[pingRTT])
    last_update_at: Optional[Time] = field(default_factory=Time)
    stats: Optional[HealthPingStats] = field(default_factory=HealthPingStats)


@dataclass(slots=True)
class pingRTT:
    time: Optional[Time] = field(default_factory=Time)
    value: Optional[str] = None
