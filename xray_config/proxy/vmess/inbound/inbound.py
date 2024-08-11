from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.common.uuid as uuid
# import xray_config.core as core
# import xray_config.features.inbound as inbound
# import xray_config.features.policy as policy
# import xray_config.features.routing as routing
# import xray_config.proxy.vmess as vmess
# import xray_config.proxy.vmess.encoding as encoding
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class userByEmail(Mutex):
    cache: Optional[dict[str, MemoryUser]] = field(default_factory=dict[str, MemoryUser])
    defaultLevel: Optional[int] = None


@dataclass(slots=True)
class Handler:
    policyManager: Optional[Manager] = field(default_factory=Manager)
    inboundHandlerManager: Optional[Manager] = field(default_factory=Manager)
    clients: Optional[TimedUserValidator] = field(default_factory=TimedUserValidator)
    usersByEmail: Optional[userByEmail] = field(default_factory=userByEmail)
    detours: Optional[DetourConfig] = field(default_factory=DetourConfig)
    sessionHistory: Optional[SessionHistory] = field(default_factory=SessionHistory)
