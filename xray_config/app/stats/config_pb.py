from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class ChannelConfig:
    blocking: Optional[bool] = None
    subscriberLimit: Optional[int] = None
    bufferSize: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
