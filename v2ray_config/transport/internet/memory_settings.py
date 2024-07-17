from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class MemoryStreamConfig:
    protocol_name: Optional[str] = None
    protocol_settings: Optional[dict] = field(default_factory=dict)
    security_type: Optional[str] = None
    security_settings: Optional[dict] = field(default_factory=dict)
    socket_settings: Optional[SocketConfig] = field(default_factory=SocketConfig)
