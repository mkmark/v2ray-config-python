from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.app.log as log
# import xray_config.common.log as log


@dataclass(slots=True)
class LogConfig:
    access: Optional[str] = None
    error: Optional[str] = None
    loglevel: Optional[str] = None
    dnsLog: Optional[bool] = None
