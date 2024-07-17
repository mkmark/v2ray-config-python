from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class matcherEntry:
    matcher: Optional[Matcher] = field(default_factory=Matcher)
    value: Optional[int] = None


@dataclass(slots=True)
class SimpleMatcherGroup:
    matchers: Optional[list[matcherEntry]] = field(default_factory=list[matcherEntry])
