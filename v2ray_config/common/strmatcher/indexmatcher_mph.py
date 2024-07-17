from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class MphIndexMatcher:
    count: Optional[int] = None
    mph: Optional[MphMatcherGroup] = field(default_factory=MphMatcherGroup)
    ac: Optional[ACAutomatonMatcherGroup] = field(default_factory=ACAutomatonMatcherGroup)
    regex: Optional[SimpleMatcherGroup] = field(default_factory=SimpleMatcherGroup)
