from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.log as log
# import v2ray_config.common.serial as serial
# import v2ray_config. as 


@dataclass(slots=True)
class ExportOption(func(*ExportOptionHolder)):
    pass


@dataclass(slots=True)
class Error:
    path_obj: Optional[dict] = field(default_factory=dict)
    prefix: Optional[list[dict]] = field(default_factory=list[dict])
    message: Optional[list[dict]] = field(default_factory=list[dict])
    inner: Optional[error] = field(default_factory=error)
    severity: Optional[Severity] = field(default_factory=Severity)


@dataclass(slots=True)
class ExportOptionHolder:
    session_id: Optional[int] = None
