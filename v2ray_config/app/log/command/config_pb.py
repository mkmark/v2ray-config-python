from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class RestartLoggerRequest:
    pass


@dataclass(slots=True)
class RestartLoggerResponse:
    pass


@dataclass(slots=True)
class FollowLogRequest:
    pass


@dataclass(slots=True)
class FollowLogResponse:
    message: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
