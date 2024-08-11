from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    host: Optional[str] = None
    path: Optional[str] = None
    header: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    accept_proxy_protocol: Optional[bool] = None
    ed: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
