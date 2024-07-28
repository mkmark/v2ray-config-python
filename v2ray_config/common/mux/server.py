from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common
# import v2ray_config.common.buf as buf
# import v2ray_config.common.errors as errors
# import v2ray_config.common.log as log
# import v2ray_config.common.net as net
# import v2ray_config.common.protocol as protocol
# import v2ray_config.common.session as session
# import v2ray_config.features.routing as routing
# import v2ray_config.transport as transport
# import v2ray_config.transport.pipe as pipe


@dataclass(slots=True)
class Server:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)


@dataclass(slots=True)
class ServerWorker:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    link: Optional[Link] = field(default_factory=Link)
    sessionManager: Optional[SessionManager] = field(default_factory=SessionManager)
