from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class ReplayFilter:
    lock: Optional[Mutex] = field(default_factory=Mutex)
    poolA: Optional[Filter] = field(default_factory=Filter)
    poolB: Optional[Filter] = field(default_factory=Filter)
    poolSwap: Optional[bool] = None
    lastSwap: Optional[int] = None
    interval: Optional[int] = None
