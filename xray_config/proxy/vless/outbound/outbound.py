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
# import xray_config.common.xudp as xudp
# import xray_config.core as core
# import xray_config.features.policy as policy
# import xray_config.proxy as proxy
# import xray_config.proxy.vless as vless
# import xray_config.proxy.vless.encoding as encoding
# import xray_config.transport as transport
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.reality as reality
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class Handler:
    serverList: Optional[ServerList] = field(default_factory=ServerList)
    serverPicker: Optional[ServerPicker] = field(default_factory=ServerPicker)
    policyManager: Optional[Manager] = field(default_factory=Manager)
    cone: Optional[bool] = None
