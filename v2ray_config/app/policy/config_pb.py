from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Second:
    value: Optional[int] = None


@dataclass(slots=True)
class SystemPolicy_Stats:
    inbound_uplink: Optional[bool] = None
    inbound_downlink: Optional[bool] = None
    outbound_uplink: Optional[bool] = None
    outbound_downlink: Optional[bool] = None


@dataclass(slots=True)
class SystemPolicy:
    stats: Optional[SystemPolicy_Stats] = field(default_factory=SystemPolicy_Stats)
    override_access_log_dest: Optional[bool] = None


@dataclass(slots=True)
class Policy_Timeout:
    handshake: Optional[Second] = field(default_factory=Second)
    connection_idle: Optional[Second] = field(default_factory=Second)
    uplink_only: Optional[Second] = field(default_factory=Second)
    downlink_only: Optional[Second] = field(default_factory=Second)


@dataclass(slots=True)
class Policy_Stats:
    user_uplink: Optional[bool] = None
    user_downlink: Optional[bool] = None


@dataclass(slots=True)
class Policy_Buffer:
    connection: Optional[int] = None


@dataclass(slots=True)
class Policy:
    timeout: Optional[Policy_Timeout] = field(default_factory=Policy_Timeout)
    stats: Optional[Policy_Stats] = field(default_factory=Policy_Stats)
    buffer: Optional[Policy_Buffer] = field(default_factory=Policy_Buffer)


@dataclass(slots=True)
class Config:
    level: Optional[dict[int, Policy]] = field(default_factory=dict[int, Policy])
    system: Optional[SystemPolicy] = field(default_factory=SystemPolicy)


@dataclass(slots=True)
class x:
    pass
