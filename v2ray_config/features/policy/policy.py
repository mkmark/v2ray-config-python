from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.platform as platform
# import v2ray_config.features as features


@dataclass(slots=True)
class policyKey(int):
    pass


@dataclass(slots=True)
class Timeout:
    handshake: Optional[str] = None
    connection_idle: Optional[str] = None
    uplink_only: Optional[str] = None
    downlink_only: Optional[str] = None


@dataclass(slots=True)
class Stats:
    user_uplink: Optional[bool] = None
    user_downlink: Optional[bool] = None


@dataclass(slots=True)
class Buffer:
    per_connection: Optional[int] = None


@dataclass(slots=True)
class SystemStats:
    inbound_uplink: Optional[bool] = None
    inbound_downlink: Optional[bool] = None
    outbound_uplink: Optional[bool] = None
    outbound_downlink: Optional[bool] = None


@dataclass(slots=True)
class System:
    stats: Optional[SystemStats] = field(default_factory=SystemStats)
    override_access_log_dest: Optional[bool] = None
    buffer: Optional[Buffer] = field(default_factory=Buffer)


@dataclass(slots=True)
class Session:
    timeouts: Optional[Timeout] = field(default_factory=Timeout)
    stats: Optional[Stats] = field(default_factory=Stats)
    buffer: Optional[Buffer] = field(default_factory=Buffer)
