from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.protocol.http as http
# import xray_config.transport.internet as internet
# import xray_config.transport.internet.stat as stat
# import xray_config.transport.internet.tls as tls


@dataclass(slots=True)
class server:
    config: Optional[Config] = field(default_factory=Config)
    addConn: Optional[ConnHandler] = field(default_factory=ConnHandler)
    innnerListener: Optional[Listener] = field(default_factory=Listener)
