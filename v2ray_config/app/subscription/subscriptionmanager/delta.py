from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class changedDocument:
    removed: Optional[list[str]] = field(default_factory=list[str])
    added: Optional[list[str]] = field(default_factory=list[str])
    modified: Optional[list[str]] = field(default_factory=list[str])
    unchanged: Optional[list[str]] = field(default_factory=list[str])
