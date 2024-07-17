from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.log as log
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.retry as retry
# import v2ray_config.common.serial as serial
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.features.dns as dns
# import v2ray_config.features.inbound as inbound
# import v2ray_config.features.policy as policy
# import v2ray_config.features.routing as routing
# import v2ray_config.proxy.vless as vless
# import v2ray_config.proxy.vless.encoding as encoding
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.tls as tls


# @dataclass(slots=True)
# class Handler:
#     inbound_handler_manager: Optional[Manager] = field(default_factory=Manager)
#     policy_manager: Optional[Manager] = field(default_factory=Manager)
#     validator: Optional[Validator] = field(default_factory=Validator)
#     dns: Optional[Client] = field(default_factory=Client)
#     fallbacks: Optional[dict[string]map[string, Fallback]] = field(default_factory=dict[string]map[string, Fallback])
