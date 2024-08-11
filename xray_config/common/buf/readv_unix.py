from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class unixReader:
    iovs: Optional[list[list[int]]] = field(default_factory=list[list[int]])
