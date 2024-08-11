from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    authority: Optional[str] = None
    service_name: Optional[str] = None
    multi_mode: Optional[bool] = None
    idle_timeout: Optional[int] = None
    health_check_timeout: Optional[int] = None
    permit_without_stream: Optional[bool] = None
    initial_windows_size: Optional[int] = None
    user_agent: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
