from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    subject_selector: Optional[list[str]] = field(default_factory=list[str])
    ping_config: Optional[HealthPingConfig] = field(default_factory=HealthPingConfig)


@dataclass(slots=True)
class HealthPingConfig:
    destination: Optional[str] = None
    connectivity: Optional[str] = None
    interval: Optional[int] = None
    sampling_count: Optional[int] = None
    timeout: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
