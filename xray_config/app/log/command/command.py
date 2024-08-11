from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.log as log
# import xray_config.common as common
# import xray_config.common.errors as errors
# import xray_config.core as core


@dataclass(slots=True)
class LoggerServer:
    v: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class service:
    v: Optional[Instance] = field(default_factory=Instance)
