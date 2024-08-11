from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.buf as buf
# import xray_config.common.errors as errors
# import xray_config.common.net as net
# import xray_config.features.routing as routing
# import xray_config.transport as transport


@dataclass(slots=True)
class Dispatcher:
    upstream: Optional[Dispatcher] = field(default_factory=Dispatcher)
