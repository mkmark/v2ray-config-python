from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.policy as policy
# import xray_config.features.routing as routing
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class Server:
    bindServer: Optional[netBindServer] = field(default_factory=netBindServer)
    info: Optional[routingInfo] = field(default_factory=routingInfo)
    policyManager: Optional[Manager] = field(default_factory=Manager)


@dataclass(slots=True)
class routingInfo:
    ctx: Optional[Context] = field(default_factory=Context)
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    inboundTag: Optional[Inbound] = field(default_factory=Inbound)
    outboundTag: Optional[Outbound] = field(default_factory=Outbound)
    contentTag: Optional[Content] = field(default_factory=Content)
