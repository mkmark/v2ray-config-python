from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ReplayFilter:
    lock: Optional[Mutex] = field(default_factory=Mutex)
    pool_a: Optional[Filter] = field(default_factory=Filter)
    pool_b: Optional[Filter] = field(default_factory=Filter)
    pool_swap: Optional[bool] = None
    last_swap: Optional[int] = None
    interval: Optional[int] = None
