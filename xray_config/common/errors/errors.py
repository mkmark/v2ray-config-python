from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.errors as errors
# import xray_config.common.ctx as ctx
# import xray_config.common.log as log
# import xray_config.common.serial as serial
# import xray_config. as 


@dataclass(slots=True)
class ExportOption(func(*ExportOptionHolder)):
    pass


@dataclass(slots=True)
class Error:
    prefix: Optional[list[dict]] = field(default_factory=list[dict])
    message: Optional[list[dict]] = field(default_factory=list[dict])
    caller: Optional[str] = None
    inner: Optional[error] = field(default_factory=error)
    severity: Optional[Severity] = field(default_factory=Severity)


@dataclass(slots=True)
class ExportOptionHolder:
    sessionID: Optional[int] = None
