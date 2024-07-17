from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.log as log
# import v2ray_config.common as common
# import v2ray_config.common.log as log


@dataclass(slots=True)
class LoggerServer:
    v: Optional[Instance] = field(default_factory=Instance)


@dataclass(slots=True)
class service:
    v: Optional[Instance] = field(default_factory=Instance)
