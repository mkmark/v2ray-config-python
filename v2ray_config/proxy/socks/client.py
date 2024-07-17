from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.retry as retry
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.features.policy as policy
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.udp as udp


# @dataclass(slots=True)
# class Client:
#     server_picker: Optional[ServerPicker] = field(default_factory=ServerPicker)
#     policy_manager: Optional[Manager] = field(default_factory=Manager)
#     version: Optional[Version] = field(default_factory=Version)
#     dns: Optional[Client] = field(default_factory=Client)
#     delay_auth_write: Optional[bool] = None
