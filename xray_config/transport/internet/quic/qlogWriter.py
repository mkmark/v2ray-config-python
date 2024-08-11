from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class QlogWriter:
    connID: Optional[ConnectionID] = field(default_factory=ConnectionID)
