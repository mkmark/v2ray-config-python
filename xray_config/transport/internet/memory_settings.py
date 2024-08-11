from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class MemoryStreamConfig:
    protocolName: Optional[str] = None
    protocolSettings: Optional[dict] = field(default_factory=dict)
    securityType: Optional[str] = None
    securitySettings: Optional[dict] = field(default_factory=dict)
    socketSettings: Optional[SocketConfig] = field(default_factory=SocketConfig)
