from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.policy as policy


@dataclass(slots=True)
class Policy:
    handshake: Optional[int] = None
    connIdle: Optional[int] = None
    uplinkOnly: Optional[int] = None
    downlinkOnly: Optional[int] = None
    statsUserUplink: Optional[bool] = None
    statsUserDownlink: Optional[bool] = None
    bufferSize: Optional[int] = None


@dataclass(slots=True)
class SystemPolicy:
    statsInboundUplink: Optional[bool] = None
    statsInboundDownlink: Optional[bool] = None
    statsOutboundUplink: Optional[bool] = None
    statsOutboundDownlink: Optional[bool] = None


@dataclass(slots=True)
class PolicyConfig:
    levels: Optional[dict[int, Policy]] = field(default_factory=dict[int, Policy])
    system: Optional[SystemPolicy] = field(default_factory=SystemPolicy)
