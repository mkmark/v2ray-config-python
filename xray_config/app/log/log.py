from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.common.log as log


@dataclass(slots=True)
class Instance(RWMutex):
    config: Optional[Config] = field(default_factory=Config)
    accessLogger: Optional[Handler] = field(default_factory=Handler)
    errorLogger: Optional[Handler] = field(default_factory=Handler)
    active: Optional[bool] = None
    dns: Optional[bool] = None
