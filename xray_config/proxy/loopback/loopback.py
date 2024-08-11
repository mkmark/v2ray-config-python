from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.common.net.cnc as cnc
# import xray_config.common.retry as retry
# import xray_config.common.session as session
# import xray_config.common.task as task
# import xray_config.core as core
# import xray_config.features.routing as routing
# import xray_config.transport as transport
# import xray_config.transport.internet as internet


@dataclass(slots=True)
class Loopback:
    config: Optional[Config] = field(default_factory=Config)
    dispatcherInstance: Optional[Dispatcher] = field(default_factory=Dispatcher)
