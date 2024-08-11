from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    path: Optional[str] = None
    abstract: Optional[bool] = None
    padding: Optional[bool] = None


@dataclass(slots=True)
class x:
    pass
