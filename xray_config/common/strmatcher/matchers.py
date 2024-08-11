from pydantic.dataclasses import dataclass, Field as field
from typing import Optional


@dataclass(slots=True)
class fullMatcher(str):
    pass


@dataclass(slots=True)
class substrMatcher(str):
    pass


@dataclass(slots=True)
class domainMatcher(str):
    pass


@dataclass(slots=True)
class regexMatcher:
    pattern: Optional[Regexp] = field(default_factory=Regexp)
