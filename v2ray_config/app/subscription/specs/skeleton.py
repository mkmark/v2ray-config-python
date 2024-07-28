from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class OutboundConfig:
    protocol: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    streamSettings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    metadata: Optional[dict[str, str]] = field(default_factory=dict[str, str])


@dataclass(slots=True)
class StreamConfig:
    transport: Optional[str] = None
    transportSettings: Optional[dict] = field(default_factory=dict)
    security: Optional[str] = None
    securitySettings: Optional[dict] = field(default_factory=dict)
