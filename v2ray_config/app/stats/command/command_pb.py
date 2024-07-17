from pydantic.dataclasses import dataclass, Field as field
from typing import Optional

# import v2ray_config.common.protoext as protoext


@dataclass(slots=True)
class GetStatsRequest:
    name: Optional[str] = None
    reset_: Optional[bool] = None


@dataclass(slots=True)
class Stat:
    name: Optional[str] = None
    value: Optional[int] = None


@dataclass(slots=True)
class GetStatsResponse:
    stat: Optional[Stat] = field(default_factory=Stat)


@dataclass(slots=True)
class QueryStatsRequest:
    pattern: Optional[str] = None
    reset_: Optional[bool] = None
    patterns: Optional[list[str]] = field(default_factory=list[str])
    regexp: Optional[bool] = None


@dataclass(slots=True)
class QueryStatsResponse:
    stat: Optional[list[Stat]] = field(default_factory=list[Stat])


@dataclass(slots=True)
class SysStatsRequest:
    pass


@dataclass(slots=True)
class SysStatsResponse:
    num_goroutine: Optional[int] = None
    num_gc: Optional[int] = None
    alloc: Optional[int] = None
    total_alloc: Optional[int] = None
    sys: Optional[int] = None
    mallocs: Optional[int] = None
    frees: Optional[int] = None
    live_objects: Optional[int] = None
    pause_total_ns: Optional[int] = None
    uptime: Optional[int] = None


@dataclass(slots=True)
class Config:
    pass


@dataclass(slots=True)
class x:
    pass
