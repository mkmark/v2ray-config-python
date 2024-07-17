from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class BloomRing(BloomRing):
    lock: Optional[Mutex] = field(default_factory=Mutex)
