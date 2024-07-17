from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class FullMatcherGroup:
    matchers: Optional[dict[string][, int]] = field(default_factory=dict[string][, int])
