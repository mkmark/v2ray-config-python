from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    version: Optional[int] = None
    padding: Optional[bool] = None
    extension: Optional[bool] = None
    csrc_count: Optional[int] = None
    marker: Optional[bool] = None
    payload_type: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
