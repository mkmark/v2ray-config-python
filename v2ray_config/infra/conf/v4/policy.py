from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.policy as policy


@dataclass(slots=True)
class Policy:
    handshake: Optional[int] = None
    conn_idle: Optional[int] = None
    uplink_only: Optional[int] = None
    downlink_only: Optional[int] = None
    stats_user_uplink: Optional[bool] = None
    stats_user_downlink: Optional[bool] = None
    buffer_size: Optional[int] = None


@dataclass(slots=True)
class SystemPolicy:
    stats_inbound_uplink: Optional[bool] = None
    stats_inbound_downlink: Optional[bool] = None
    stats_outbound_uplink: Optional[bool] = None
    stats_outbound_downlink: Optional[bool] = None
    override_access_log_dest: Optional[bool] = None


@dataclass(slots=True)
class PolicyConfig:
    levels: Optional[dict[int, Policy]] = field(default_factory=dict[int, Policy])
    system: Optional[SystemPolicy] = field(default_factory=SystemPolicy)
