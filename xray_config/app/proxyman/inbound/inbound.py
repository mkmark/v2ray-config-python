from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.proxyman as proxyman
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.serial as serial
# import xray_config.common.session as session
# import xray_config.core as core
# import xray_config.features.inbound as inbound


@dataclass(slots=True)
class Manager:
    access: Optional[RWMutex] = field(default_factory=RWMutex)
    untaggedHandler: Optional[list[Handler]] = field(default_factory=list[Handler])
    taggedHandlers: Optional[dict[str, Handler]] = field(default_factory=dict[str, Handler])
    running: Optional[bool] = None
