from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class StreamConfig:
    transport: Optional[str] = None
    transport_settings: Optional[dict] = field(default_factory=dict)
    security: Optional[str] = None
    security_settings: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class OutboundConfig:
    protocol: Optional[str] = None
    settings: Optional[dict] = field(default_factory=dict)
    stream_settings: Optional[StreamConfig] = field(default_factory=StreamConfig)
    metadata: Optional[dict[str, str]] = field(default_factory=dict[str, str])
