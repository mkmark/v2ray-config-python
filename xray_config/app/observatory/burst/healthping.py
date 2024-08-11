from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.dice as dice
# import xray_config.common.errors as errors


@dataclass(slots=True)
class HealthPingSettings:
    destination: Optional[str] = None
    connectivity: Optional[str] = None
    interval: Optional[str] = None
    sampling: Optional[int] = None
    timeout: Optional[str] = None


@dataclass(slots=True)
class HealthPing:
    ctx: Optional[Context] = field(default_factory=Context)
    access: Optional[Mutex] = field(default_factory=Mutex)
    ticker: Optional[Ticker] = field(default_factory=Ticker)
    tickerClose: Optional[chan] = field(default_factory=chan)
    settings: Optional[HealthPingSettings] = field(default_factory=HealthPingSettings)
    results: Optional[dict[str, HealthPingRTTS]] = field(default_factory=dict[str, HealthPingRTTS])


@dataclass(slots=True)
class rtt:
    handler: Optional[str] = None
    value: Optional[str] = None
