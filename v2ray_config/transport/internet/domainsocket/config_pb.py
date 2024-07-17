from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class Config:
    path: Optional[str] = None
    abstract: Optional[bool] = None
    padding: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
