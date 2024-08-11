from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.log as log
# import xray_config.common.net as net
# import xray_config.common.protocol as protocol
# import xray_config.common.protocol.http as http
# import xray_config.common.session as session
# import xray_config.common.signal as signal
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.policy as policy
# import xray_config.features.routing as routing
# import xray_config.transport.internet.stat as stat


@dataclass(slots=True)
class Server:
    config: Optional[ServerConfig] = field(default_factory=ServerConfig)
    policyManager: Optional[Manager] = field(default_factory=Manager)


@dataclass(slots=True)
class readerOnly(Reader):
    pass
