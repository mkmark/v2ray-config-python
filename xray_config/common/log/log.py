from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.log as log
# import xray_config.common.serial as serial


@dataclass(slots=True)
class GeneralMessage:
    severity: Optional[Severity] = field(default_factory=Severity)
    content: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class syncHandler(RWMutex, Handler):
    pass
