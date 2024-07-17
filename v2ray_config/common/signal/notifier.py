from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Notifier:
    c: Optional[chan] = field(default_factory=chan)
