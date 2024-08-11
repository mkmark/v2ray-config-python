from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class Type(int):
    pass


@dataclass(slots=True)
class matcherEntry:
    m: Optional[Matcher] = field(default_factory=Matcher)
    id: Optional[int] = None


@dataclass(slots=True)
class MatcherGroup:
    count: Optional[int] = None
    fullMatcher: Optional[FullMatcherGroup] = field(default_factory=FullMatcherGroup)
    domainMatcher: Optional[DomainMatcherGroup] = field(default_factory=DomainMatcherGroup)
    otherMatchers: Optional[list[matcherEntry]] = field(default_factory=list[matcherEntry])
