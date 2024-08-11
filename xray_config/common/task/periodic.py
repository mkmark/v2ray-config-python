from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Periodic:
    interval: Optional[str] = None
    access: Optional[Mutex] = field(default_factory=Mutex)
    timer: Optional[Timer] = field(default_factory=Timer)
    running: Optional[bool] = None
