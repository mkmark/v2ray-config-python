from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.signal.done as done
# import xray_config.core as core
# import xray_config.features.outbound as outbound


@dataclass(slots=True)
class Commander(Mutex):
    server: Optional[Server] = field(default_factory=Server)
    services: Optional[list[Service]] = field(default_factory=list[Service])
    ohm: Optional[Manager] = field(default_factory=Manager)
    tag: Optional[str] = None
    listen: Optional[str] = None
