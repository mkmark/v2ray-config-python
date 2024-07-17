from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class requestSaltWithLength:
    length: Optional[int] = None
    content: Optional[list[int]] = field(default_factory=list[int])
