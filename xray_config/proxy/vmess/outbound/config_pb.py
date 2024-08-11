from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.protocol as protocol


@dataclass(slots=True)
class Config:
    receiver: Optional[list[ServerEndpoint]] = field(default_factory=list[ServerEndpoint])


@dataclass(slots=True)
class x:
    pass
