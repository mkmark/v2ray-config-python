from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Config:
    show: Optional[bool] = None
    dest: Optional[str] = None
    type: Optional[str] = None
    xver: Optional[int] = None
    server_names: Optional[list[str]] = field(default_factory=list[str])
    private_key: Optional[list[int]] = field(default_factory=list[int])
    min_client_ver: Optional[list[int]] = field(default_factory=list[int])
    max_client_ver: Optional[list[int]] = field(default_factory=list[int])
    max_time_diff: Optional[int] = None
    short_ids: Optional[list[list[int]]] = field(default_factory=list[list[int]])
    fingerprint: Optional[str] = None
    server_name: Optional[str] = None
    public_key: Optional[list[int]] = field(default_factory=list[int])
    short_id: Optional[list[int]] = field(default_factory=list[int])
    spider_x: Optional[str] = None
    spider_y: Optional[list[int]] = field(default_factory=list[int])
    master_key_log: Optional[str] = None


@dataclass(slots=True)
class x:
    pass
