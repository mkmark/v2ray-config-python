from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.retry as retry
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.features.policy as policy
# import v2ray_config.proxy as proxy
# import v2ray_config.proxy.vless as vless
# import v2ray_config.proxy.vless.encoding as encoding
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet


@dataclass(slots=True)
class Handler:
    serverList: Optional[ServerList] = field(default_factory=ServerList)
    serverPicker: Optional[ServerPicker] = field(default_factory=ServerPicker)
    policyManager: Optional[Manager] = field(default_factory=Manager)
