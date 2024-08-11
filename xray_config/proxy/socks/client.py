from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.retry as retry
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.dns as dns
# import xray_config.features.policy as policy
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class Client:
    serverPicker: Optional[ServerPicker] = field(default_factory=ServerPicker)
    policyManager: Optional[Manager] = field(default_factory=Manager)
    version: Optional[Version] = field(default_factory=Version)
    dns: Optional[Client] = field(default_factory=Client)
