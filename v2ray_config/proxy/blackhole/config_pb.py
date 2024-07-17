from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class NoneResponse:
    pass


@dataclass(slots=True)
class HTTPResponse:
    pass


@dataclass(slots=True)
class Config:
    response: Optional[Any] = field(default_factory=Any)


@dataclass(slots=True)
class SimplifiedConfig:
    pass


@dataclass(slots=True)
class x:
    pass
