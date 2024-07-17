from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common as common


@dataclass(slots=True)
class Request:
    data: Optional[list[int]] = field(default_factory=list[int])
    connection_tag: Optional[list[int]] = field(default_factory=list[int])


@dataclass(slots=True)
class Response:
    data: Optional[list[int]] = field(default_factory=list[int])
