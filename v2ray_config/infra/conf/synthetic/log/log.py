from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.app.log as log
# import v2ray_config.common.log as log


@dataclass(slots=True)
class LogConfig:
    access: Optional[str] = None
    error: Optional[str] = None
    loglevel: Optional[str] = None
