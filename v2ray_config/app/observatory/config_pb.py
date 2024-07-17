from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class ObservationResult:
    status: Optional[list[OutboundStatus]] = field(default_factory=list[OutboundStatus])


@dataclass(slots=True)
class HealthPingMeasurementResult:
    all: Optional[int] = None
    fail: Optional[int] = None
    deviation: Optional[int] = None
    average: Optional[int] = None
    max: Optional[int] = None
    min: Optional[int] = None


@dataclass(slots=True)
class OutboundStatus:
    alive: Optional[bool] = None
    delay: Optional[int] = None
    last_error_reason: Optional[str] = None
    outbound_tag: Optional[str] = None
    last_seen_time: Optional[int] = None
    last_try_time: Optional[int] = None
    health_ping: Optional[HealthPingMeasurementResult] = field(default_factory=HealthPingMeasurementResult)


@dataclass(slots=True)
class ProbeResult:
    alive: Optional[bool] = None
    delay: Optional[int] = None
    last_error_reason: Optional[str] = None


@dataclass(slots=True)
class Intensity:
    probe_interval: Optional[int] = None


@dataclass(slots=True)
class Config:
    subject_selector: Optional[list[str]] = field(default_factory=list[str])
    probe_url: Optional[str] = None
    probe_interval: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
