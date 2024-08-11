from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    host: Optional[str] = None
    path: Optional[str] = None
    header: Optional[dict[str, str]] = field(default_factory=dict[str, str])
    scMaxConcurrentPosts: Optional[RandRangeConfig] = field(default_factory=RandRangeConfig)
    scMaxEachPostBytes: Optional[RandRangeConfig] = field(default_factory=RandRangeConfig)
    scMinPostsIntervalMs: Optional[RandRangeConfig] = field(default_factory=RandRangeConfig)
    noSSEHeader: Optional[bool] = None
    responseOkPadding: Optional[RandRangeConfig] = field(default_factory=RandRangeConfig)


@dataclass(slots=True)
class RandRangeConfig:
    from_: Optional[int] = None
    to: Optional[int] = None


@dataclass(slots=True)
class x:
    pass
