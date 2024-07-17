from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Instance:
    token: Optional[chan] = field(default_factory=chan)
