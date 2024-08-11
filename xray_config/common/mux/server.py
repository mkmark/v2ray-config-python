from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.session as session
# import xray_config.core as core
# import xray_config.features.routing as routing
# import xray_config.transport as transport
# import xray_config.transport.pipe as pipe


@dataclass(slots=True)
class Server:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)


@dataclass(slots=True)
class ServerWorker:
    dispatcher: Optional[Dispatcher] = field(default_factory=Dispatcher)
    link: Optional[Link] = field(default_factory=Link)
    sessionManager: Optional[SessionManager] = field(default_factory=SessionManager)
