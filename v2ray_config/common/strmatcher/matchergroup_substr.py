from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class SubstrMatcherGroup:
    patterns: Optional[list[str]] = field(default_factory=list[str])
    values: Optional[list[int]] = field(default_factory=list[int])
