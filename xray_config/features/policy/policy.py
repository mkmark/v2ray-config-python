from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.platform as platform
# import xray_config.features as features


@dataclass(slots=True)
class policyKey(int):
    pass


@dataclass(slots=True)
class Timeout:
    handshake: Optional[str] = None
    connectionIdle: Optional[str] = None
    uplinkOnly: Optional[str] = None
    downlinkOnly: Optional[str] = None


@dataclass(slots=True)
class Stats:
    userUplink: Optional[bool] = None
    userDownlink: Optional[bool] = None


@dataclass(slots=True)
class Buffer:
    perConnection: Optional[int] = None


@dataclass(slots=True)
class SystemStats:
    inboundUplink: Optional[bool] = None
    inboundDownlink: Optional[bool] = None
    outboundUplink: Optional[bool] = None
    outboundDownlink: Optional[bool] = None


@dataclass(slots=True)
class System:
    stats: Optional[SystemStats] = field(default_factory=SystemStats)
    buffer: Optional[Buffer] = field(default_factory=Buffer)


@dataclass(slots=True)
class Session:
    timeouts: Optional[Timeout] = field(default_factory=Timeout)
    stats: Optional[Stats] = field(default_factory=Stats)
    buffer: Optional[Buffer] = field(default_factory=Buffer)
