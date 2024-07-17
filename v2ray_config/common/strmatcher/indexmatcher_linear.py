from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class LinearIndexMatcher:
    count: Optional[int] = None
    full: Optional[FullMatcherGroup] = field(default_factory=FullMatcherGroup)
    domain: Optional[DomainMatcherGroup] = field(default_factory=DomainMatcherGroup)
    substr: Optional[SubstrMatcherGroup] = field(default_factory=SubstrMatcherGroup)
    regex: Optional[SimpleMatcherGroup] = field(default_factory=SimpleMatcherGroup)
