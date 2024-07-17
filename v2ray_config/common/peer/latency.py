from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class AverageLatency:
    access: Optional[Mutex] = field(default_factory=Mutex)
    value: Optional[int] = None
