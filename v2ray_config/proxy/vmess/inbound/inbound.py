from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.log as log
# import v2ray_config.common.net as net
# import v2ray_config.common.platform as platform
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.common.uuid as uuid
# import v2ray_config.features.inbound as inbound
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing
# import v2ray_config.proxy.vmess as vmess
# import v2ray_config.proxy.vmess.encoding as encoding
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class userByEmail(Mutex):
    cache: Optional[dict[str, MemoryUser]] = field(default_factory=dict[str, MemoryUser])
    defaultLevel: Optional[int] = None
    defaultAlterIDs: Optional[int] = None


@dataclass(slots=True)
class Handler:
    policyManager: Optional[Manager] = field(default_factory=Manager)
    inboundHandlerManager: Optional[Manager] = field(default_factory=Manager)
    clients: Optional[TimedUserValidator] = field(default_factory=TimedUserValidator)
    usersByEmail: Optional[userByEmail] = field(default_factory=userByEmail)
    detours: Optional[DetourConfig] = field(default_factory=DetourConfig)
    sessionHistory: Optional[SessionHistory] = field(default_factory=SessionHistory)
    secure: Optional[bool] = None
