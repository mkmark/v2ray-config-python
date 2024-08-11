from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import xray_config.common.serial as serial


@dataclass(slots=True)
class NoneResponse:
    pass


@dataclass(slots=True)
class HTTPResponse:
    pass


@dataclass(slots=True)
class Config:
    response: Optional[dict] = field(default_factory=dict)


@dataclass(slots=True)
class x:
    pass
