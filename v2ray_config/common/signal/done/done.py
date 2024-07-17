from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Instance:
    access: Optional[Mutex] = field(default_factory=Mutex)
    c: Optional[chan] = field(default_factory=chan)
    closed: Optional[bool] = None
