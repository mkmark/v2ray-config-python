from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.environment as environment
# import v2ray_config.common.environment.envctx as envctx
# import v2ray_config.common.net as net
# import v2ray_config.common.net.packetaddr as packetaddr
# import v2ray_config.common.retry as retry
# import v2ray_config.common.session as session
# import v2ray_config.common.signal as signal
# import v2ray_config.common.task as task
# import v2ray_config.transport as transport
# import v2ray_config.transport.internet as internet
# import v2ray_config.transport.internet.udp as udp


# @dataclass(slots=True)
# class Client:
#     config: Optional[ClientConfig] = field(default_factory=ClientConfig)
#     ctx: Optional[Context] = field(default_factory=Context)


# @dataclass(slots=True)
# class ClientUDPConnState:
#     session: Optional[ClientUDPSession] = field(default_factory=ClientUDPSession)
#     init_once: Optional[Once] = field(default_factory=Once)
